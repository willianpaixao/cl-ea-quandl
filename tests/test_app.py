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


if __name__ == '__main__':
    # Calling pytest directly instead of the CLI
    pytest.main()
