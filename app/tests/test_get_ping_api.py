# coding: utf-8

from fastapi.testclient import TestClient


from web.models.get_ping_response import GetPingResponse  # noqa: F401


def test_get_ping(client: TestClient):
    """Test case for get_ping

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/ping",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200

