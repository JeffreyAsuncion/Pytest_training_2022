from ast import main
import pytest
import requests
import json

@pytest.fixture
def main_url():
    return "http://reqres.in"

def test_login_valid(main_url):
    url = main_url + "/api/login/"
    data = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token["token"] == "QpwL5tke4Pnpja7X"