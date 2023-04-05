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
from web.models.banner import Banner


router = APIRouter()


@router.get(
    "/banners",
    responses={
        200: {"model": List[Banner], "description": "success"},
    },
    tags=["get_banners"],
    response_model_by_alias=True,
)
async def get_banners(
) -> List[Banner]:
    return [
        Banner(id='1', imageURL='https://dodopizza.ru/SeoSnippetImages/ru-snippet.jpg'),
        Banner(id='2', imageURL='https://dodopizza.ru/SeoSnippetImages/ru-snippet.jpg'),
        Banner(id='3', imageURL='https://dodopizza.ru/SeoSnippetImages/ru-snippet.jpg')
    ]
