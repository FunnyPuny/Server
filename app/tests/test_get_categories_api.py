# coding: utf-8

from fastapi.testclient import TestClient


from web.models.category import Category  # noqa: F401


def test_get_categories(client: TestClient):
    """Test case for get_categories

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/categories",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200

