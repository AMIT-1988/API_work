import requests

# Define the API endpoint URL
url = "https://api.sportmonks.com/v3/core/countries/1161?api_token=MeXYvpmiUUDCyK2p5LIO2hZfn5FBzxMzQWAeTxFz5dEpz3T4igMtML9dMZ4J"

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response data
    data = response.json()
    
    # Do something with the data
    print(data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")