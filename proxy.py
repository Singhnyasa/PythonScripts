#Watch video of codeWithHarry

import requests

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              
            }

r = requests.get("https://httpbin.org/get", proxies=proxies)
print(r.text)