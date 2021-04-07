import argparse


class Request:
    """
    """

    def __init__(self, args_: argparse.Namespace):
        args_as_dict = vars(args_)
        self._mode = args_as_dict.get("mode")
        self._inputfile = args_as_dict.get("inputfile")
        self._inputdata = args_as_dict.get("inputdata")
        self._expanded = args_as_dict.get("expanded")
        self._output = args_as_dict.get("output")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def inputfile(self):
        return self._inputfile

    @inputfile.setter
    def inputfile(self, value):
        self._inputfile = value

    @property
    def inputdata(self):
        return self._inputdata

    @inputdata.setter
    def inputdata(self, value):
        self._inputdata = value

    @property
    def expanded(self):
        return self._expanded

    @expanded.setter
    def expanded(self, value):
        self._expanded = value

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    def __str__(self) -> str:
        return f"Request Object: \n\tMode:{self._mode} \n\t" \
               f"InputFile: {self._inputfile}\n\tInputData: {self._inputdata}\n\t" \
               f"Expanded: {self._expanded}\n\tOutput: {self._output}"
