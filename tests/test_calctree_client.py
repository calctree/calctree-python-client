import json
import unittest
from unittest.mock import MagicMock, patch

from src.calctree.client import CalcTreeClient

backend_response = b'[{"id":"1aba0a13-d5bb-41fb-ba4b-6abfc7ac97a3","createdDate":"2024-01-19T05:23:58.230Z","updatedDate":"2024-01-19T05:40:57.444Z","title":"cylinder_radius","formula":100,"value":100,"type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"m\\"},\\"description\\":\\"\\"}","deletedAt":null,"mappingItem":null,"formulaVariables":[]},{"id":"bacc0657-ee00-432a-bb50-b7d748ecf5af","createdDate":"2024-01-19T05:25:17.724Z","updatedDate":"2024-01-19T06:11:06.447Z","title":"capacity","formula":1000,"value":1000,"type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"L\\"}}","deletedAt":null,"mappingItem":null,"formulaVariables":[]},{"id":"b05e521c-8a4e-47a0-8669-4daa0fcff1de","createdDate":"2024-01-19T05:36:43.407Z","updatedDate":"2024-01-19T06:11:06.447Z","title":"cylinder_height","formula":"=_b278fdd42e9444abb37198ee8269787a/pow(_3b6cf2da30cb46cd89ab84635a1115e5,2)","value":0.1,"type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2}}","deletedAt":null,"mappingItem":null,"formulaVariables":[{"id":"2ae06efa-10d5-4d6c-9b39-82957951bd83","createdDate":"2024-01-19T05:37:08.518Z","updatedDate":"2024-01-19T05:37:08.518Z","title":"_b278fdd42e9444abb37198ee8269787a","sourceCell":{"id":"bacc0657-ee00-432a-bb50-b7d748ecf5af","createdDate":"2024-01-19T05:25:17.724Z","updatedDate":"2024-01-19T06:11:06.447Z","title":"capacity","formula":"1000","value":"1000","type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"L\\"}}","deletedAt":null}},{"id":"48859b1b-5712-42fa-ac7d-dc35ed307690","createdDate":"2024-01-19T05:37:08.528Z","updatedDate":"2024-01-19T05:37:08.528Z","title":"_3b6cf2da30cb46cd89ab84635a1115e5","sourceCell":{"id":"1aba0a13-d5bb-41fb-ba4b-6abfc7ac97a3","createdDate":"2024-01-19T05:23:58.230Z","updatedDate":"2024-01-19T05:40:57.444Z","title":"cylinder_radius","formula":"10","value":"10","type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"m\\"},\\"description\\":\\"\\"}","deletedAt":null}}]}]'  # noqa: E501
expected_client_response = [
    {"name": "cylinder_radius", "value": "100"},
    {"name": "capacity", "value": "1000"},
    {"name": "cylinder_height", "value": "0.1"}
]


class TestCalcTreeClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_api_key"
        self.client = CalcTreeClient(self.api_key)

    @patch("urllib.request.urlopen")
    def test_request_calculation_success(self, mock_urlopen):
        ct_cells = [{"name": "capacity", "formula": "1000"}]
        page_id = "12345"

        mock_response = MagicMock()
        mock_read = MagicMock()
        mock_read.return_value = backend_response
        mock_response_return_obj = mock_response.__enter__.return_value
        mock_response_return_obj.read = mock_read
        mock_response_return_obj.status = 200

        mock_urlopen.return_value = mock_response

        client_response = self.client.run_calculation(page_id, ct_cells)

        for expected_item, actual_item in zip(expected_client_response, client_response):
            self.assertEqual(expected_item["name"], actual_item["name"])
            self.assertEqual(expected_item["value"], actual_item["value"])

    @patch("urllib.request.urlopen")
    def test_request_calculation_failure(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Custom error message")

        with self.assertRaises(Exception):
            self.client.run_calculation('123', [])

    @patch("urllib.request.urlopen")
    def test_raises_an_exception_on_404_status_code(self, mock_urlopen):
        invalid_response = b'"param": "invalid" "value": "response"'
        mock_response = MagicMock()
        mock_read = MagicMock()
        mock_read.return_value = invalid_response
        mock_response_return_obj = mock_response.__enter__.return_value
        mock_response_return_obj.read = mock_read
        mock_response_return_obj.status = 404

        mock_urlopen.return_value = mock_response

        with self.assertRaises(Exception):
            self.client.run_calculation('123', [])

    @patch("urllib.request.urlopen")
    def test_raises_an_exception_on_500_status_code(self, mock_urlopen):
        invalid_response = b'"param": "invalid" "value": "response"'
        mock_response = MagicMock()
        mock_read = MagicMock()
        mock_read.return_value = invalid_response
        mock_response_return_obj = mock_response.__enter__.return_value
        mock_response_return_obj.read = mock_read
        mock_response_return_obj.status = 500

        mock_urlopen.return_value = mock_response

        with self.assertRaises(Exception):
            self.client.run_calculation('123', [])

    @patch("urllib.request.urlopen")
    def test_request_calculation_invalid_json(self, mock_urlopen):
        invalid_response = b'"param": "invalid" "value": "response"'
        mock_response = MagicMock()
        mock_read = MagicMock()
        mock_read.return_value = invalid_response
        mock_response_return_obj = mock_response.__enter__.return_value
        mock_response_return_obj.read = mock_read
        mock_response_return_obj.status = 200

        mock_urlopen.return_value = mock_response

        with self.assertRaises(json.JSONDecodeError):
            self.client.run_calculation('123', [])
