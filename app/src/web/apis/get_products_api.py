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
        Product(id='1', name='Ветчина и грибы', description="Ветчина, шампиньоны, увеличенная порция моцареллы, томатный соус ", categoryId='1', price='345', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQesvEgwP7BHghHiOMfEwKsXU0xg7HBH-c6Fw&usqp=CAU'),
        Product(id='2', name='Баварские колбаски', description='Баварские колбаски, ветчина, пикантная пепперони, острая чоризо, моцарелла, томатный соус', categoryId='1', price='345', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5nNgE0Lk_5ioxioe0HO3T8NwDP1ls5rKm3A&usqp=CAU'),
        Product(id='3', name='Лосось с томатами', description='Лосось, томаты черри, моцарелла, соус песто', categoryId='1', price='350', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQesvEgwP7BHghHiOMfEwKsXU0xg7HBH-c6Fw&usqp=CAU'),
        Product(id='4', name='3 пиццы от 799 руб', description='Три маленькие пиццы по супермене. Цена комбо зависит от выбранных пицц', categoryId='2', price='799', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5nNgE0Lk_5ioxioe0HO3T8NwDP1ls5rKm3A&usqp=CAU'),
        Product(id='5', name='Чизкейк Нью-Йорк ', description='Мы перепробовали тысячу\ndesert и наконец нашли любимца гостей - нежнейший творожный чизкейк', categoryId='3', price='100', imageURL='https://e7.pngegg.com/pngimages/384/1003/png-clipart-kfc-cheesecake-chicken-krasnoyarsk-ice-cream-chicken-food-animals.png'),
        Product(id='6', name='Coca-Cola', description='Освежающий напиток', categoryId='4', price='100', imageURL='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS75WZOG9323Cn88YXDGGp7eZmz7ZPGJsacZQ&usqp=CAU')
    ]
