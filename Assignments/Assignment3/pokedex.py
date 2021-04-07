import argparse
import request
from pokeretriever import async_request, pokedex_object, mode_enum
import asyncio
from facade_pokeretriever import FacadePokeretriever
import sys


def setup_command_line() -> request.Request:
    parser = argparse.ArgumentParser(prog="Pokedex")
    parser.add_argument('mode', choices=["pokemon", "ability", "move"])
    mutually_exclusive = parser.add_mutually_exclusive_group(required=True)
    mutually_exclusive.add_argument('--inputfile', action='store')
    mutually_exclusive.add_argument('--inputdata', action='store')
    parser.add_argument("--expanded", action='store_true')
    parser.add_argument("--output", action='store')
    args = parser.parse_args()
    return request.Request(args)


def main():
    request = setup_command_line()
    FacadePokeretriever.execute_request(request)



if __name__ == '__main__':
    main()
