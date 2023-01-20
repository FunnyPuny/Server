# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from web.models.extra_models import TokenModel  # noqa: F401
from web.models.get_ping_response import GetPingResponse


router = APIRouter()


@router.get(
    "/ping",
    responses={
        200: {"model": GetPingResponse, "description": "success"},
    },
    tags=["get_ping"],
    response_model_by_alias=True,
)
async def get_ping(
) -> GetPingResponse:
    return GetPingResponse(status='ok')
