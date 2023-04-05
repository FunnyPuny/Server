# coding: utf-8

"""
    OpenAPI FunnyPuny

    This is api for server FunnyPuny

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from web.apis.get_ping_api import router as GetPingApiRouter
from web.apis.get_banners_api import router as GetBannerApiRouter
from web.apis.get_categories_api import router as GetCategoriesApiRouter
from web.apis.get_products_api import router as GetProductsApiRouter

app = FastAPI(
    title="OpenAPI FunnyPuny",
    description="This is api for server FunnyPuny",
    version="1.0.0",
)

app.include_router(GetPingApiRouter)
app.include_router(GetBannerApiRouter)
app.include_router(GetCategoriesApiRouter)
app.include_router(GetProductsApiRouter)
