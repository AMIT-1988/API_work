import requests

# Define the API endpoint URL
url = "https://api.sportmonks.com/v3/core/countries?api_token=zbzaHmvJh3TAa7Ta4CeZp1fI5Tqck7HT7kjYdWWAAkUU7YOYbICnhXL2jAPz&include=leagues;"

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

