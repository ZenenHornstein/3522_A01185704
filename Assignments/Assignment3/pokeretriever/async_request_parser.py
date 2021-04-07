import abc
from .pokedex_object import Stat, Move, Ability, Pokemon
from .url_enum import urlEnum
import asyncio
from .async_request import process_requests

import sys
import aiohttp


class AsyncRequestParser(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def parse_response(response: dict):
        """
        Parse the regular API response.

        :param response:
        :return:
        """
        pass

    @staticmethod
    def parse_extended_response(response: dict):
        """
        Parse the expanded api response.

        :param response:
        :return:
        """
        pass


class StatParser(AsyncRequestParser):
    def __init__(self):
        super().__init__()

    @staticmethod
    def parse_response(request: dict) -> list[Stat]:
        """
        Parse the regular stat response that is recieved when quering pokemon api without --expanded flag.
        :param request:
        :return:
        """
        result_list = []
        stat_list = request.get('stats')
        for i in stat_list:
            stat_name = i['stat']['name']
            stat_url = i['stat']['url']
            base_stat = i['base_stat']
            result_list.append(Stat(name=stat_name, id_=None, base_value=base_stat, url=stat_url))
        return result_list

    @staticmethod
    def parse_extended_response_and_mutate(request: dict, stat_to_mutate: Stat):
        """
        Mutates an existing stat object by calling the appropriate api subquery and adding the additional information
        :param request:
        :param stat_to_mutate:
        :return: the mutate Stat object
        """
        stat_name = request.get("name")
        stat_id = request.get('id')
        stat_is_battle_only = request.get("is_battle_only")

        stat_to_mutate.id = stat_id
        stat_to_mutate.name = stat_name
        stat_to_mutate.is_battle_only = stat_is_battle_only
        return stat_to_mutate


class AbilityParser(AsyncRequestParser):
    def __init__(self):
        super().__init__()

    @staticmethod
    def parse_response(response: dict) -> Ability:
        """
        parse the regular ability response recieved when quering pokemon without expanded flag.

        :param response:
        :return:
        """
        result_list = []
        ability_list = response['abilities']
        for i in ability_list:
            ablility_name = i['ability']['name']
            result_list.append(Ability(name=ablility_name))
        return result_list

    @staticmethod
    def parse_extended_response(response: dict) -> Ability:
        """
        parse the extended ability response recieved when quering pokemon with expanded flag or ability endpoint.

        :param response:
        :return:
        """
        id_ = response['id']
        name = response['name']
        generation = response['generation']['name']
        effect = [i['effect'] for i in response['effect_entries'] if i['language']['name'] == 'en']
        effect_short = [i['short_effect'] for i in response['effect_entries'] if i['language']['name'] == 'en']
        pokemon = [x['pokemon']['name'] for x in response['pokemon']]
        return Ability(name, id_, generation, effect, effect_short, pokemon)


class MoveParser(AsyncRequestParser):
    def __init__(self):
        super().__init__()

    @staticmethod
    def parse_response(response: dict) -> Move:
        """
        Parses the regular move api response that is sent when querying the pokemon API.
        :param response:
        :return:
        """
        result_list = []
        moves_list = response['moves']

        for i in moves_list:
            move_name = i['move']['name']
            level_aquired = i["version_group_details"][0]['level_learned_at']
            result_list.append(Move(name=move_name, level_aquired=level_aquired))
        return result_list

    @staticmethod
    def parse_extended_response(response: dict) -> Move:
        """
        Parses the extended Move api response that is recieved either in move mode or in pokemon mode with --expanded flag
        :param response: the response recieved from asyncRequest
        :return: the Move object with additional information from subquery
        """
        name = response['name']
        id_ = response['id']
        generation = response['generation']['name']
        accuracy = response['accuracy']
        pp = response['pp']
        power = response['power']
        type = response['type']['name']
        damage_class = response['damage_class']['name']
        effect = [i['short_effect'] for i in response['effect_entries'] if i['language']['name'] == 'en']
        return Move(name, id_, generation, accuracy, pp, power, type, effect_short=effect, damage_class=damage_class)


class PokemonParser(AsyncRequestParser):
    @staticmethod
    def parse_response(response: dict):
        """
        Parses the vanilla pokemon request. called when mode=pokemon and the --expanded flag is NOT supplied

        :param response: the response recieved from asyncRequest
        :return: the Pokemon object
        """
        name = response['name']
        id_ = response['id']
        height = response['height']
        weight = response['weight']
        stats = StatParser.parse_response(response)  ## something special here
        types = response['types']
        abilites = AbilityParser.parse_response(response)  ## something special here
        moves = MoveParser.parse_response(response)  ## Something special here
        return (Pokemon(name=name, id_=id_, height=height,
                        weight=weight, stats=stats, types=types,
                        abilities=abilites, moves=moves))

    @staticmethod
    def parse_extended_response(response: dict):
        """
        This method parses a single pokemon object and subqieries the stats and ablities and moves.
        returns a full pokemon expanded object.

        :param response:
        :return:

        """

        name = response['name']
        id_ = response['id']
        height = response['height']
        weight = response['weight']
        stats = StatParser.parse_response(response)  ## something special here
        types = response['types']
        abilities = AbilityParser.parse_response(response)  ## something special here
        moves = MoveParser.parse_response(response)  ## Something special here

        stats_id_list = [stat.url.split("/")[-2] for stat in stats]
        abilities_name_list = [ability.name for ability in abilities]
        moves_name_list = [move.name for move in moves]

        loop = asyncio.get_event_loop()

        results = loop.run_until_complete(process_requests(requests=stats_id_list, url=urlEnum.STAT_URL.value))
        extended_stats_objects = [StatParser.parse_extended_response_and_mutate(x, y) for x, y in zip(results, stats)]

        results = loop.run_until_complete(process_requests(requests=abilities_name_list, url=urlEnum.ABILITY_URL.value))
        extended_ability_objects = [AbilityParser.parse_extended_response(x) for x in results]

        results = loop.run_until_complete(process_requests(requests=moves_name_list, url=urlEnum.MOVE_URL.value))
        extended_moves_objects = [MoveParser.parse_extended_response(x) for x in results]

        return Pokemon(name=name, id_=id_, height=height, weight=weight, stats=extended_stats_objects, types=types,
                       abilities=extended_ability_objects, moves=extended_moves_objects)


def main():
    pass


if __name__ == '__main__':
    main()
