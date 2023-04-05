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
        Product(id='2', name='Сырная', description='Моцарелла, сыры чеддер и пармезан, фирменный соус альфредо', categoryId='1', price='345', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/d9c609f1422247f2b87b6293eb461ff0_584x584.webp'),
        Product(id='3', name='Лосось с томатами', description='Лосось, томаты черри, моцарелла, соус песто', categoryId='1', price='350', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/d7bbbc4c74af442e8b9b3ea2faf3c941_584x584.webp'),
        Product(id='4', name='3 пиццы от 799 руб', description='Три маленькие пиццы по супер цене. Цена комбо зависит от выбранных пицц', categoryId='2', price='799', imageURL='https://dodopizza-a.akamaihd.net/static/Img/ComboTemplates/6896b1e6b27f42aba9012121ec13948e_584x584.webp'),
        Product(id='13', name='2 пиццы', description='Парочка что надо. 2 средние пиццы. Цена комбо зависит от выбранных пицц и может быть увеличена', categoryId='2', price='989', imageURL='https://dodopizza-a.akamaihd.net/static/Img/ComboTemplates/519b674d1d4243439ee192703b348497_584x584.webp'),
        Product(id='14', name='7 пицц', description='7 — счастливое число, особенно если речь о 7 средних пиццах на компанию 15-20 человек', categoryId='2', price='3359', imageURL='https://dodopizza-a.akamaihd.net/static/Img/ComboTemplates/663573d68a3a484f92955346eb6d862d_584x584.webp'),
        Product(id='15', name='2 Додстера', description='Кручу-верчу, два горячих Додстера хочу! ', categoryId='2', price='319', imageURL='https://dodopizza-a.akamaihd.net/static/Img/ComboTemplates/9b7e7191f3e84b88b276b7253bf34996_584x584.webp'),
        Product(id='5', name='Чизкейк Нью-Йорк ', description='Мы перепробовали тысячу\ndesert и наконец нашли любимца гостей - нежнейший творожный чизкейк', categoryId='3', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/5a06bd533bb846f59cfb4b8c4e062f86_584x584.webp'),
        Product(id='6', name='Маффин Соленая карамель ', description='Раз откусить — навсегда полюбить!\nОцените яркое сочетание соленой карамели и арахиса', categoryId='3', price='95', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/c3687909a9cf4064aabc5b07a166e848_584x584.webp'),
        Product(id='7', name='Шоколадный кукис ', description='На вид печенье как планета, а на вкус — шоколадная комета с глазурью', categoryId='3', price='95', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/32e5d56e679748839eba187f1690ca67_1875x1875.webp'),
        Product(id='8', name='Чизкейк Банановый с шоколадным печеньем ', description='Солнечный снаружи и яркий по вкусу внутри. Летняя новинка — нежныйк', categoryId='3', price='149', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/543c6e4479c24db29427d74efde5151c_1875x1875.webp'),
        Product(id='9', name='Coca-Cola', description='Освежающий напиток', categoryId='4', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/dc74c00bc0634933ba7194b99a164094_584x584.webp'),
        Product(id='10', name='Coca-Cola Zero', description='Освежающий напиток', categoryId='4', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/665800efd5614d4eb6b3b8ec2eb4d662_584x584.webp'),
        Product(id='11', name='Fanta', description='Освежающий напиток', categoryId='4', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/f501c8e65f574f00bc7ab6ec4720e602_584x584.webp'),
        Product(id='12', name='Sprite', description='Освежающий напиток', categoryId='4', price='100', imageURL='https://dodopizza-a.akamaihd.net/static/Img/Products/b25b40c2bf934265ae4eea61a2617d1a_584x584.webp')
    ]
