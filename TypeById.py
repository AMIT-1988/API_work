import http.client

conn = http.client.HTTPSConnection("api.sportmonks.com")
payload = ''
headers = {}
conn.request("GET", "/v3/core/countries?api_token=zbzaHmvJh3TAa7Ta4CeZp1fI5Tqck7HT7kjYdWWAAkUU7YOYbICnhXL2jAPz", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))