import pytest

from app import create_app


def test_config(app):
    """Test create_app without passing test config."""
    assert create_app().testing


def test_call_adapter(client):
    rv = client.post('/', json={'id': '1', 'data': {}})
    json_data = rv.get_json()
    assert json_data.get('statusCode') == 500
    assert json_data.get('status') == 'errored'


def test_request_fred(client):
    rv = client.post('/', json={"id": 1, "data": {"dataset": "FRED/GDP"}})
    json_data = rv.get_json()
    assert json_data.get('statusCode') == 200
    assert 'result' in json_data
    rv = client.post('/', json={"id": 2, "data": {"dataset": "FRED/UNRATE", "rows": 2}})
    json_data = rv.get_json()
    assert json_data.get('statusCode') == 200
    assert 'result' in json_data


def test_extra_params(client):
    rv = client.post('/', json={"id": "01acef78e00f45ca911f9202124fbabf",
                                "data":{
                                    "address":"0x795FB736ef447f649EBD462F35d6cC8437925fC0",
                                    "dataset": "FRED/UNRATE"
                                }})
    json_data = rv.get_json()
    assert json_data.get('statusCode') == 200
    assert 'result' in json_data


if __name__ == '__main__':
    # Calling pytest directly instead of the CLI
    pytest.main()
