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

```python
import json

from calctree.client import CalcTreeClient

client = CalcTreeClient('YOUR_API_KEY')

res = client.run_calculation("6fd16232-39e3-44a9-aee2-d6ad375698b0",
                             [{"name": "cylinder_radius", "formula": "1000"}]
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

