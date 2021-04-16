import aiohttp
import asyncio
from .url_enum import urlEnum
from .pokedex_object import Pokemon, Move


async def get_pokemon_api(id_: int, url: str, session: aiohttp.ClientSession) -> dict:
    """
    Run a single async query of any type
    :param id_: id of a pokemon ability or move
    :param url: the url endpoint
    :param session: aiohttp.ClientSession
    :return: response as a dict
    """
    target_url = url.format(id_)
    response = await session.request(method="GET", url=target_url)
    json_dict = await response.json()
    return json_dict

async def process_requests(requests: list, url: str) -> list:
    """
    This function depicts the use of asyncio.gather to run multiple
    async coroutines concurrently.
    :param requests: a list of int's
    :return: list of dict, collection of response data from the endpoint.
    """

    async with aiohttp.ClientSession() as session:
        async_coroutines = [get_pokemon_api(id_, url, session)
                            for id_ in requests]

        responses = await asyncio.gather(*async_coroutines)
        return responses

