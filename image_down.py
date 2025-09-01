import requests


url = 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

response = requests.get(url)
fb = open("img.jpeg", "wb")
fb.write(response.content)
fb.close()

 