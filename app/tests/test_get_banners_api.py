# coding: utf-8

from fastapi.testclient import TestClient


from web.models.banner import Banner  # noqa: F401


def test_get_banners(client: TestClient):
    """Test case for get_banners

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/banners",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200

