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
        Product(id='1', name='Ветчина и грибы', description="Ветчина, шампиньоны, увеличенная порция моцареллы, томатный соус ", categoryId='1', price='345', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/0c24c7c195574d7cae45c889bd8043fc_584x584.webp'),
        Product(id='2', name='Баварские колбаски', description='Баварские колбаски, ветчина, пикантная пепперони, острая чоризо, моцарелла, томатный соус', categoryId='1', price='345', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5nNgE0Lk_5ioxioe0HO3T8NwDP1ls5rKm3A&usqp=CAU'),
        Product(id='3', name='Лосось с томатами', description='Лосось, томаты черри, моцарелла, соус песто', categoryId='1', price='350', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/d7bbbc4c74af442e8b9b3ea2faf3c941_584x584.webp'),
        Product(id='4', name='3 пиццы от 799 руб', description='Три маленькие пиццы по супермене. Цена комбо зависит от выбранных пицц', categoryId='2', price='799', imageURL='https://dodopizza-a.akamaihd.net/static/Img/ComboTemplates/6896b1e6b27f42aba9012121ec13948e_584x584.webp'),
        Product(id='5', name='Чизкейк Нью-Йорк ', description='Мы перепробовали тысячу\ndesert и наконец нашли любимца гостей - нежнейший творожный чизкейк', categoryId='3', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/5a06bd533bb846f59cfb4b8c4e062f86_584x584.webp'),
        Product(id='6', name='Coca-Cola', description='Освежающий напиток', categoryId='4', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/dc74c00bc0634933ba7194b99a164094_584x584.webp')
    ]
