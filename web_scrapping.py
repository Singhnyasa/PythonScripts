import requests
from urllib.parse import urlparse
import os
# Data Collection
links = [
    "https://www.codewitharry.com/blog",
    "https://www.codewitharry.com/videos",
    "https://www.codewitharry.com/contact"
]

os.makedirs("htmls" , exist_ok=True)

try:
 for link in links:
     r =requests.get(link)

     path = urlparse(link).path.strip('/')

     filename = path if path else 'index'
     with open(f"htmls/{filename}.html" , "w") as f:
        f.write(r.text)
        print(f"Saved : {filename}.html")
except requests.RequestException as e:
   print(f"Failed to fetch link as {e}")