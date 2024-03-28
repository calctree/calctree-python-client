# CalcTree Python Client
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/calctree/calctree-python-client/CI)

The CalcTree Python Client is a Python library that provides a convenient interface for interacting with the CalcTree API. It allows you to perform calculations using CalcTree's powerful calculation engine.

## Installation

You can install the CalcTree Python Client using pip:

```bash
pip install calctree
```

# Getting Started
To use the CalcTree Python Client, you need to obtain an API key from CalcTree. Once you have your API key, you can initialize the client and start running calculations.

Remember to replace YOUR_API_KEY with your actual API key, YOUR_PAGE_ID with the ID of the page you want to run calculations on, and YOUR_PARAM_NAME with the name of the parameter you want to set the value for.

```python
import json

from calctree.client import CalcTreeClient

client = CalcTreeClient('YOUR_API_KEY')

res = client.run_calculation("YOUR_PAGE_ID",
                             [{"name": "YOUR_PARAM_NAME", "formula": "1000"}]
                             )

print("Result as a dictionary:")
print(result.to_dict())

print("Value of param 'cylinder_radius':")
print(result.get_param_value("cylinder_radius"))

print("List of params:")
print(result.get_params())

print("List of values:")
print(result.get_values())
```

