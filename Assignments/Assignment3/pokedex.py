import argparse
import request
from aiohttp.client_exceptions import ContentTypeError
from pokeretriever import async_request, pokedex_object, mode_enum
import asyncio
from facade_pokeretriever import FacadePokeretriever
import pathlib
import sys


class InvalidFileTypeError(Exception):
    """
    The exception to be raised if a extension not supported by File extensions is requested.
    """
    def __init__(self, my_msg):
        super().__init__(my_msg)

def setup_command_line() -> request.Request:
    parser = argparse.ArgumentParser(prog="Pokedex")
    parser.add_argument('mode', choices=["pokemon", "ability", "move"])
    mutually_exclusive = parser.add_mutually_exclusive_group(required=True)
    mutually_exclusive.add_argument('--inputfile', action='store')
    mutually_exclusive.add_argument('--inputdata', action='store')
    parser.add_argument("--expanded", action='store_true')
    parser.add_argument("--output", action='store')
    args = parser.parse_args()

    args_as_dict = vars(args)

    if args_as_dict.get("inputfile"):
        if pathlib.Path(args_as_dict['inputfile']).suffix != ".txt":
            raise InvalidFileTypeError(f'File {args_as_dict["inputfile"]} does not have .txt extension')

    return request.Request(args)


def main():
    request = setup_command_line()
    try:
        FacadePokeretriever.execute_request(request)
    except ContentTypeError as e:
        print("Something went wrong! please ensure your input source is correct!")




if __name__ == '__main__':
    main()
