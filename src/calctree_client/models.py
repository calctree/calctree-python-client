class CTCell:
    """Represents a parameter in a CalcTree page calculation.

    Parameters:
        param (str): The parameter name, the same as on the page.
        value (str): The value associated with the parameter.

    Attributes:
        param (str): The parameter name.
        value (str): The value associated with the parameter.
    """

    def __init__(self, param: str, value: str):
        self.param: str = param
        self.value: str = value

    def to_dict(self):
        return {"param": self.param, "value": self.value}


class CalculationResultItem:
    """Represents an item in the calculation result.

    Attributes:
        param (str): The parameter name.
        value (str): The value associated with the parameter.
    """

    def __init__(self, param: str, value: str):
        self.param: str = param
        self.value: str = value
