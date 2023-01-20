# coding: utf-8

import pytest
import json
from aiohttp import web

from src.models.get_ping_response import GetPingResponse


async def test_get_ping(client):
    """Test case for get_ping

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

