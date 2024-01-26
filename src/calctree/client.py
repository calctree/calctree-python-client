import json
from urllib import request


class CalcTreeClient:
    """Client for interacting with the CalcTree API.

    This client allows you to perform calculations using the CalcTree API.

    Args:
        api_key (str): The API key for authentication.

    Attributes:
        _api_key (str): The API key for authentication.
    """

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._calctree_host = 'https://api.calctree.com'
        self._run_calculation_endpoint = '/api/calctree-cell/run-calculation'

    def run_calculation(self, page_id: str, ct_cells, host: str = 'https://api.calctree.com'):
        """Run a calculation using the CalcTree API.

        Args:
            page_id (str): The ID of the page containing the calculation.
            ct_cells (List[Parameters]): A list of Parameters instances representing the calculation parameters.
                Each Parameters instance has the following attributes:
                    name (str): The parameter name, the same as on the page.
                    formula (str): The value associated with the parameter.

        Returns:
            List[Attributes]: A list of Attributes instances representing the calculation result.
                Each Attributes instance has the following attributes:
                    name (str): The parameter name.
                    value (str): The value associated with the parameter.
        """  # noqa
        calculation_request_response = self._request_calculation(ct_cells, page_id)
        return self._process_response(calculation_request_response)

    def _process_response(self, response):
        calculation_result = json.loads(response)
        return [{'name': j['title'], 'value': str(j['value'])} for j in calculation_result]

    def _request_calculation(self, ct_cells, page_id: str):
        url = f'{self._calctree_host}{self._run_calculation_endpoint}'
        headers = self._prepare_headers()
        body = self._prepare_body(ct_cells, page_id)

        payload = json.dumps(body).encode('utf-8')

        req = request.Request(url, payload, headers)
        with request.urlopen(req) as request_result:  # noqa
            self._raise_exception_for_failed_request(request_result)
            return request_result.read()

    def _raise_exception_for_failed_request(self, request_result):
        if not (200 <= request_result.status < 300):
            error_message = request_result.read().decode('utf-8')
            raise Exception(f'HTTP request failed with status code {request_result.status}: {error_message}')

    def _prepare_body(self, ct_cells, page_id: str):
        return {
            'pageId': page_id,
            'ctCells': ct_cells,
        }

    def _prepare_headers(self):
        return {
            'x-api-key': self._api_key,
            'content-type': 'application/json',
        }
