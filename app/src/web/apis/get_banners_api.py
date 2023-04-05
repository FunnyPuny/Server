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
        Banner(id='2', imageURL='https://cdn.dodostatic.net/static/Img/BonusActionBanners/Gallery/g_1678721107_b96b4d3189a44bf4966de96b848e75fa.jpeg'),
        Banner(id='3', imageURL='https://cdn.dodostatic.net/static/Img/BonusActionBanners/Gallery/g_1642653583_ee54149010ab4dcf8f55e2bdd98f8d5d.jpeg'),
        Banner(id='4', imageURL='https://cdn.dodostatic.net/static/Img/BonusActionBanners/Gallery/g_1678730080_3ddc392e7b3d44a18ee262f7dfc774ec.jpeg'),
        Banner(id='5', imageURL='https://cdn.dodostatic.net/static/Img/BonusActionBanners/Gallery/g_1622432276_59229e58ab644a78b0eb593b7cb937c0.jpeg')
    ]
