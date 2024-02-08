import json
from urllib import request

# Set connection properties
url = "https://api.calctree.com/api/calctree-cell/run-calculation"
headers = {
    "x-api-key": "YOUR_API_KEY",  # Replace YOUR_API_KEY with your API key
    "content-type": "application/json"
}

# Define the request payload
body = {
    "pageId": "6fd16232-39e3-44a9-aee2-d6ad375698b0",
    # PageId - the ID of the page on which you'd like to run the calculation.
    "ctCells": [
        {"name": "cylinder_radius", "formula": "100"},  # set value=100 of 'cylinder_radius' parameter
    ]
}
request_payload = json.dumps(body).encode("utf8")

# Send the request
req = request.Request(url, request_payload, headers)
res = request.urlopen(req)
output = res.read()

# Load the result from the response
response_payload = json.loads(output)

print(response_payload)
