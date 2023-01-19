import pytest
import requests
import settings


class Fixtures:
    def pingRequest(self):
        return requests.get(settings.HOST + settings.REQUEST).status_code


@pytest.fixture()
def mock_backend():
    return Fixtures()



