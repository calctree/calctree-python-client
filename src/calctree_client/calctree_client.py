import json
from typing import List
from urllib import request

from src.calctree_client.models import CTCell, CalculationResultItem


class CalcTreeClient:
    """Client for interacting with the CalcTree API.

    This client allows you to perform calculations using the CalcTree API.

    Args:
        api_key (str): The API key for authentication.

    Attributes:
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def run_calculation(self, page_id: str, ct_cells: List[CTCell],
                        host: str = "https://api.calctree.com") -> List[CalculationResultItem]:
        """Run a calculation using the CalcTree API.

                Args:
                    page_id (str): The ID of the page containing the calculation.
                    ct_cells (List[CTCell]): A list of CTCell instances representing the calculation parameters.
                    host (str, optional): The API host. Defaults to "https://api.calctree.com".

                Returns:
                    List[CalculationResultItem]: A list of CalculationResultItem instances representing the calculation
                    result.
        """
        calculation_request_response = self._request_calculation(ct_cells, host, page_id)
        return self._process_response(calculation_request_response)

    def _process_response(self, response) -> List[CalculationResultItem]:
        calculation_result = json.loads(response)
        return [CalculationResultItem(param=j["title"], value=str(j["value"])) for j in calculation_result]

    def _request_calculation(self, ct_cells: List[CTCell], host: str, page_id: str):
        url = f"{host}/api/calctree-cell/run-calculation"
        headers = self._prepare_headers()
        body = self._prepare_body(ct_cells, page_id)

        payload = json.dumps(body).encode("utf-8")

        req = request.Request(url, payload, headers)
        with request.urlopen(req) as request_result:
            request_result.raise_for_status()
            return request_result.read()

    def _prepare_body(self, ct_cells: List[CTCell], page_id: str):
        return {
            "pageId": page_id,
            "ctCells": [cell.to_dict() for cell in ct_cells]
        }

    def _prepare_headers(self):
        return {
            "x-api-key": self.api_key,
            "content-type": "application/json"
        }
