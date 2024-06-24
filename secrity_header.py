import requests
from bs4 import BeautifulSoup

#Strict-Transport-Security: max-age=31536000 ; includeSubDomains
sec_head=['X-Frame-Options','Strict-Transport-Security','X-XSS-Protection','X-Content-Type-Options','Content-Security-Policy','X-Permitted-Cross-Domain-Policies','Referrer-Policy']

def check_secruity_headers(website):
 try:
  req=requests.get(website)
  headers=req.headers
  for i in sec_head:
   if i in headers:
    pass
   else:
    print("Missing secrurity Header:"+i)
 except:
 	pass

#check_secruity_headers("http://testphp.vulnweb.com/")