"""
Please note that this example requires you to install the CalcTreeClient dependency before you can use it.
"""

from calctree.client import CalcTreeClient

# Create a client
client = CalcTreeClient('YOUR_API_KEY')

# Run calculation on page '6fd16232-39e3-44a9-aee2-d6ad375698b0' with a parameter 'cylinder_radius' value of '100'.
result = client.run_calculation(
    "6fd16232-39e3-44a9-aee2-d6ad375698b0",
    [
        {"name": "cylinder_radius", "formula": "100"},
    ]
)

print(result)
