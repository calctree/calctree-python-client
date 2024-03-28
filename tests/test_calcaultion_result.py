import unittest

from src.calctree.calculation_result import CalculationResult
from src.calctree.exceptions import ParameterNotFoundException

backend_response = b'[{"id":"1aba0a13-d5bb-41fb-ba4b-6abfc7ac97a3","createdDate":"2024-01-19T05:23:58.230Z","updatedDate":"2024-01-19T05:40:57.444Z","title":"cylinder_radius","formula":100,"value":100,"type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"m\\"},\\"description\\":\\"\\"}","deletedAt":null,"mappingItem":null,"formulaVariables":[]},{"id":"bacc0657-ee00-432a-bb50-b7d748ecf5af","createdDate":"2024-01-19T05:25:17.724Z","updatedDate":"2024-01-19T06:11:06.447Z","title":"capacity","formula":1000,"value":1000,"type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"L\\"}}","deletedAt":null,"mappingItem":null,"formulaVariables":[]},{"id":"b05e521c-8a4e-47a0-8669-4daa0fcff1de","createdDate":"2024-01-19T05:36:43.407Z","updatedDate":"2024-01-19T06:11:06.447Z","title":"cylinder_height","formula":"=_b278fdd42e9444abb37198ee8269787a/pow(_3b6cf2da30cb46cd89ab84635a1115e5,2)","value":0.1,"type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2}}","deletedAt":null,"mappingItem":null,"formulaVariables":[{"id":"2ae06efa-10d5-4d6c-9b39-82957951bd83","createdDate":"2024-01-19T05:37:08.518Z","updatedDate":"2024-01-19T05:37:08.518Z","title":"_b278fdd42e9444abb37198ee8269787a","sourceCell":{"id":"bacc0657-ee00-432a-bb50-b7d748ecf5af","createdDate":"2024-01-19T05:25:17.724Z","updatedDate":"2024-01-19T06:11:06.447Z","title":"capacity","formula":"1000","value":"1000","type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"L\\"}}","deletedAt":null}},{"id":"48859b1b-5712-42fa-ac7d-dc35ed307690","createdDate":"2024-01-19T05:37:08.528Z","updatedDate":"2024-01-19T05:37:08.528Z","title":"_3b6cf2da30cb46cd89ab84635a1115e5","sourceCell":{"id":"1aba0a13-d5bb-41fb-ba4b-6abfc7ac97a3","createdDate":"2024-01-19T05:23:58.230Z","updatedDate":"2024-01-19T05:40:57.444Z","title":"cylinder_radius","formula":"10","value":"10","type":"MATHJS","pageId":"6fd16232-39e3-44a9-aee2-d6ad375698b0","mappingItemId":null,"errorMessage":null,"settings":"{\\"format\\":{\\"type\\":\\"number\\",\\"separator\\":\\",\\",\\"precision\\":2,\\"unit\\":\\"m\\"},\\"description\\":\\"\\"}","deletedAt":null}}]}]'  # noqa: E501
expected_dict = [
    {"name": "cylinder_radius", "value": "100"},
    {"name": "capacity", "value": "1000"},
    {"name": "cylinder_height", "value": "0.1"}
]


class TestCalculationResult(unittest.TestCase):

    def test_get_param_value(self):
        calculation_result = CalculationResult(backend_response)
        self.assertEqual(calculation_result.get_param_value("cylinder_radius"), "100")
        self.assertEqual(calculation_result.get_param_value("capacity"), "1000")
        self.assertEqual(calculation_result.get_param_value("cylinder_height"), "0.1")
        with self.assertRaises(ParameterNotFoundException):
            calculation_result.get_param_value("invalid_param")

    def test_get_params(self):
        calculation_result = CalculationResult(backend_response)
        self.assertEqual(calculation_result.get_params(), ["cylinder_radius", "capacity", "cylinder_height"])

    def test_get_values(self):
        calculation_result = CalculationResult(backend_response)
        self.assertEqual(calculation_result.get_values(), ["100", "1000", "0.1"])

    def test_to_dict(self):
        calculation_result = CalculationResult(backend_response)
        self.assertEqual(calculation_result.to_dict(), expected_dict)
