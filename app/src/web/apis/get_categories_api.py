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
from web.models.category import Category


router = APIRouter()


@router.get(
    "/categories",
    responses={
        200: {"model": List[Category], "description": "success"},
    },
    tags=["get_categories"],
    response_model_by_alias=True,
)
async def get_categories(
) -> List[Category]:
    return [
        Category(id='1', name='Пицца'),
        Category(id='2', name='Комбо'),
        Category(id='3', name='Десерты'),
        Category(id='4', name='Напитки')
    ]
