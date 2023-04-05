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
from web.models.product import Product


router = APIRouter()


@router.get(
    "/products",
    responses={
        200: {"model": List[Product], "description": "success"},
    },
    tags=["get_products"],
    response_model_by_alias=True,
)
async def get_products(
) -> List[Product]:
    return [
        Product(id='1', name='Ветчина и грибы', description="Ветчина, шампиньоны, увеличенная порция моцареллы, томатный соус ", categoryId='1', price='345', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQesvEgwP7BHghHiOMfEwKsXU0xg7HBH-c6Fw&usqp=CAU')
    ]
