import requests

url = 'https://en.wikipedia.org/wiki/Example'
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print(content)
else:
    print('An error occurred:', response.status_code)