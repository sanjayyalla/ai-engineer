import pytest
import requests
import source.api_mocking as api_mocking
import unittest.mock as mock

@mock.patch("requests.get")
def test_get_data(api_mocking_test):
    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"id":"1"}

    api_mocking_test.return_value = mock_resp
    data = api_mocking.get_data()
    assert {"id":"1"} == data


@mock.patch("requests.get")
def test_get_data_error(mock_get):
    mock_resp = mock.Mock()
    mock_resp.status_code = 400
    mock_get.return_value = mock_resp
    with pytest.raises(requests.HTTPError):
        api_mocking.get_data()
        

    