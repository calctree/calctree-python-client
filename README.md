# CalcTree Python Client
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/calctree/calctree-python-client/CI)

The CalcTree Python Client is a Python library that provides a convenient interface for interacting with the CalcTree API. It allows you to perform calculations using CalcTree's powerful calculation engine.

## Installation

You can install the CalcTree Python Client using pip:

```bash
pip install calctree-python-client
```

# Getting Started
To use the CalcTree Python Client, you need to obtain an API key from CalcTree. Once you have your API key, you can initialize the client and start running calculations.

```python
from src.calctree_client.calctree_client import CalcTreeClient
from src.calctree_client.models import CTCell

# Replace 'your_api_key' with your actual CalcTree API key
api_key = 'your_api_key'

# Initialize the CalcTree client
client = CalcTreeClient(api_key)

# Define your calculation parameters using CTCell instances
ct_cells = [
    CTCell(param="capacity", value="1000"),
    CTCell(param="cylinder_radius", value="10")
]

# Run a calculation
page_id = '6fd16232-39e3-44a9-aee2-d6ad375698b0'
calculation_result = client.run_calculation(page_id, ct_cells)

# Print the result
for result_item in calculation_result:
    print(f"{result_item.param}: {result_item.value}")
```

