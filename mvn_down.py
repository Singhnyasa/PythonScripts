import requests

url = 'https://dlcdn.apache.org/maven/maven-3/3.9.11/binaries/apache-maven-3.9.11-bin.zip'

res = requests.get(url)

fb = open('mvn.zip', 'wb')
fb.write(res.content)
fb.close()
