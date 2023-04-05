# coding: utf-8

from fastapi.testclient import TestClient


from web.models.product import Product  # noqa: F401


def test_get_products(client: TestClient):
    """Test case for get_products

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/products",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200

