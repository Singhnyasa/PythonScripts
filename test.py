import requests

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response = requests.get(url)
indexs = response.json()
 
print(response.status_code)

for i in range(len(indexs)):
    print(indexs[i]["user"]["login"])