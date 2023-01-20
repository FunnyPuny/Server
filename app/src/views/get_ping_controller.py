from typing import List, Dict
from aiohttp import web

from src.models.get_ping_response import GetPingResponse
from src import util


async def get_ping(request: web.Request, ) -> web.Response:
    """get_ping

    


    """
    return web.Response(status=200)
