from request import Request
from pokeretriever import AsyncRequest
from pokeretriever.ModeEnum import modeEnum
from pokeretriever.urlEnum import urlEnum

from pokeretriever.AsyncRequestParser import StatParser, MoveParser, AbilityParser, PokemonParser
from pokeretriever.PokedexObject import Stat, Move, Pokemon, Ability
import asyncio
import sys


class FacadePokeretriever:
    def __init__(self):
        pass

    @staticmethod
    def execute_request(request: Request):

        PARSER_MAPPER = {
            "pokemon":PokemonParser,
            "ability": AbilityParser,
            "move": MoveParser
        }

        URL_MAPPER = {
            "pokemon": urlEnum.POKEMON_URL.value,
            "ability": urlEnum.ABILITY_URL.value,
            "move": urlEnum.MOVE_URL.value
        }

        parser = PARSER_MAPPER[request.mode]
        target_url = URL_MAPPER[request.mode]
        loop = asyncio.get_event_loop()


       #No input file but input data
        if request.inputdata and not request.inputfile:
            print("Request inputdata")
            request.inputdata = [request.inputdata]
            results = loop.run_until_complete(AsyncRequest.process_requests(request.inputdata, url=target_url))
            results = [parser.parse_extended_response(x) for x in results]


        #Input file
        if request.inputfile and not request.inputdata:
            with open(request.inputfile, "r", encoding='utf-8') as infile:
                querys = infile.readlines()
                querys = [i.strip() for i in querys]
                request.inputdata = querys
                results = loop.run_until_complete(AsyncRequest.process_requests(querys, url=target_url))
                results = [parser.parse_extended_response(x) for x in results]


        if request.inputfile and not request.expanded and request.mode == modeEnum.POKEMON.value:
            print("HERE IS INPUT FILE AND NOT EXPANDED AND POKEMON")
            results = loop.run_until_complete(AsyncRequest.process_requests(querys, url=target_url))
            results = [parser.parse_response(x) for x in results]

        if request.inputfile and request.expanded and request.mode == modeEnum.POKEMON.value:
            print("HERE IS INPUT FILE AND EXPANDED AND POKEMON")
            results = loop.run_until_complete(AsyncRequest.process_requests(querys, url=target_url))
            results = [parser.parse_extended_response(x) for x in results]



        # Out put results in a report
        for i in results:
            i.display_summary(print_loc=sys.stdout)


