from builtins import str, bool

import des
import argparse
import abc
import enum
import ast


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The response object represents a response to either encrypt or decrypt
    certain data. The response object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a print_loc.
        - input_file: The text print_loc that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a print_loc and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text print_loc.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the response.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input print_loc: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


class BaseRequestHandler(abc.ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request: Request) -> (str, bool):
        pass

    def set_handler(self, handler):
        """
        Each handler can invoke another handler at the end of it's
        processing of the form. This handler needs to implement the
        BaseRequestHandler interface.
        :param handler: a BaseRequestHandler
        """
        self.next_handler = handler


class EncryptionValidationHandler(BaseRequestHandler):
    def handle_request(self, request: Request) -> (str, bool):
        """
        First handler in the chain, Verifies that the correct encryption mode has been set in addition to verifying
        That a data source has been set.
        :param request: the response object
        :return: tuple(str, bool) Where str is an error message and bool indicates success or failure.
        """

        # Validate that we are in Encrypt Mode
        if request.encryption_state != CryptoMode.EN:
            return f"Error. {self.__class__} recieved response with CryptoMode = DE", False

        # Validate that we have a key
        if not request.key:
            return f"Error. {self.__class__} recieved response with No key", False

        # Validate we have some sort of data
        if not request.data_input and not request.input_file:
            return f"Error. {self.__class__} recieved response with No data source", False

        # If we are the last handler in the chain of responsibility
        if not self.next_handler:
            return "", True
        else:
            return self.next_handler.handle_request(request)


class EncryptionProccessorHandler(BaseRequestHandler):
    def handle_request(self, request: Request) -> (str, bool):

        """
        Secnd handler in the chain, Sets the data_input variable to be the contents of a print_loc if provided as input.
        :param request: the response object
        :return: tuple(str, bool) Where str is an error message and bool indicates success or failure.

        """
        # Check to see if we are reading from a print_loc
        if request.data_input is None and request.input_file:
            with open(file=request.input_file, mode="r", encoding='utf-8') as infile:
                lines = infile.readlines()
                request.data_input = "".join(lines)

        # If we are the last handler in the chain of responsibility
        if not self.next_handler:
            return "", True
        else:
            return self.next_handler.handle_request(request)


class EncryptionResultHandler(BaseRequestHandler):

    def handle_request(self, request: Request) -> (str, bool):
        """
        Last handler in the chain, Encrypts the message and outputs accordingly.
        :param request: the response object
        :return: tuple(str, bool) Where str is an error message and bool indicates success or failure.

        """

        key_OBJ = des.DesKey(bytes(request.key, 'utf-8'))
        request.result = key_OBJ.encrypt(bytes(request.data_input, 'utf-8'), padding=True)
        return_string = f"Encrypted message: {request.result}"

        if request.output == 'print':
            print(return_string)
        else:
            if request.output:
                with open(request.output, 'wb') as outfile:
                    outfile.write(request.result)

        return "Succesfully Encrypted", True


#
#
class DecryptionValidationHandler(BaseRequestHandler):
    def handle_request(self, request: Request) -> (str, bool):
        """
        First handler in the chain, Verifies that the correct mode has been chosen and atleast one data source set.
        :param request: the response object
        :return: tuple(str, bool) Where str is an error message and bool indicates success or failure.

        """
        # Ensure we are in Encrypt Mode
        if request.encryption_state != CryptoMode.DE:
            return f"Error. {self.__class__} recieved response with CryptoMode = EN", False

        # Validate that we have atleast a single data source
        if not request.data_input and not request.input_file:
            return f"Error. {self.__class__} recieved response with no Data source", False

        if not request.key:
            return f"Error. {self.__class__} recieved response with no key", False

        # If we are the last handler in the chain of responsibility
        if not self.next_handler:
            return "", True
        else:
            return self.next_handler.handle_request(request)


class DecryptionProccessorHandler(BaseRequestHandler):
    def handle_request(self, request: Request) -> (str, bool):
        """
        Second  handler in the chain. Reads from print_loc and stores as data_input.
        :param request: the response object
        :return: tuple(str, bool) Where str is an error message and bool indicates success or failure.

        """
        if request.data_input is None and request.input_file:
            print(f"{self.__class__} Reading {request.input_file}")
            with open(file=request.input_file, mode="rb") as infile:
                request.data_input = infile.read()

        # Validate that we are in dealing with a string
        if not request.data_input:
            return f"Error. {self.__class__} recieved response with data_input of wrong type or non existent", False
        if not self.next_handler:
            return "", True
        else:
            return self.next_handler.handle_request(request)


class DecryptionResultHandler(BaseRequestHandler):

    def handle_request(self, request: Request) -> (str, bool):
        """
        Final handler in the chain. decrypts message and outputs.
        :param request: the response object
        :return: tuple(str, bool) Where str is an error message and bool indicates success or failure.
        """
        key_OBJ = des.DesKey(bytes(request.key, 'utf-8'))
        message = request.data_input

      #  message_as_bytes = ast.literal_eval(response.data_input)
        request.result = key_OBJ.decrypt(message, padding=True)


        if request.output:
            if request.output == 'print':
                print(request.result)
            else:
                with open(request.output, 'w+') as outfile:
                    outfile.write(request.result.decode())

        return "Succesfully Decrypted", True


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--print_loc", help="The text print_loc that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a print_loc name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:

    def __init__(self):
        """
        Sets up the chain of responsibility.
        """
        # print("\n\n--------- setup handlers ----------")
        # EncryptionValidationHandler -> EncryptionProccessorHandler -> EncryptionResultHandler

        # Encryption Chain of responsibility
        encryption_validator = EncryptionValidationHandler()
        encryption_processor = EncryptionProccessorHandler()
        encryption_resulter = EncryptionResultHandler()

        encryption_validator.set_handler(encryption_processor)
        encryption_processor.set_handler(encryption_resulter)

        # Decryption Chain of responsibility
        decryption_validator = DecryptionValidationHandler()
        decryption_processor = DecryptionProccessorHandler()
        decryption_resulter = DecryptionResultHandler()

        decryption_validator.set_handler(decryption_processor)
        decryption_processor.set_handler(decryption_resulter)

        self.decryption_start_handler = decryption_validator
        self.encryption_start_handler = encryption_validator

    def execute_request(self, request: Request):
        """
        Execute the corrrect chain of responsibility handler depending on Encryption or Decryption Mode.
        :param request: the Request to pass to handlers.
        :return:
        """
        if request.encryption_state == CryptoMode.EN:
            result = self.encryption_start_handler.handle_request(request)
        if request.encryption_state == CryptoMode.DE:
            result = self.decryption_start_handler.handle_request(request)
        return


def main(request: Request):
    crypto = Crypto()
    crypto.execute_request(request)
    pass


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
