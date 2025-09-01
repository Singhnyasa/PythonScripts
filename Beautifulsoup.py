import os 
from bs4 import BeautifulSoup

for file in os.listdir("htmls"):
    with open(f"htmls/{file}") as f:
        htmlcontent = f.read()
        soup = BeautifulSoup(htmlcontent, "html.parser")
        # print(soup)
    for link in soup.find_all("link"):
         print(link.get("href"))   

 

