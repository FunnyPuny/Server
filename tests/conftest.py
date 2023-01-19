import pytest
import requests
import settings

@pytest.fixture()
def pingRequest():
    return requests.get(settings.HOST + settings.REQUEST).status_code

