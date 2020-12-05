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


if __name__ == '__main__':
    # Calling pytest directly instead of the CLI
    pytest.main()
