import json
from typing import List

from exceptions import ParameterNotFoundException


class CalculationResult:
    """
    Represents the result of a calculation performed by the CalcTree API.
    """

    def __init__(self, api_response):
        calculation_result = json.loads(api_response)
        self.result = [{'name': j['title'], 'value': str(j['value'])} for j in calculation_result]

    def get_param_value(self, param_name) -> str:
        """
        Get the value of a parameter in the calculation result.
        Args:
            param_name(str): The name of the parameter.

        Returns:
            str: The value of the parameter.
        """
        script_output = next((item for item in self.result if item.get('name') == param_name), None)
        if script_output is None:
            raise ParameterNotFoundException(f'Parameter {param_name} not found in the calculation result')
        return script_output['value']

    def get_params(self) -> List[str]:
        """
        Get the names of the parameters in the calculation result.

        Returns:
            List[str]: The names of the parameters.
        """
        return list(map(lambda x: x['name'], self.result))

    def get_values(self) -> List[str]:
        """
        Get the values of the parameters in the calculation result.

        Returns:
            List[str]: The values of the parameters.
        """
        return list(map(lambda x: x['value'], self.result))

    def to_dict(self):
        """
        Get the calculation result as a list of dictionaries.
        :return:
             list[dict[str, str]]: The calculation result as a list of dictionaries.
        """
        return self.result
