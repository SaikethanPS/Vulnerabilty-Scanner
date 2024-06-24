import requests
from bs4 import BeautifulSoup

def check_subdomain(website):
 try:
  website=website.replace("http://",'')
  website=website.replace('https://','')
  website=website.replace('/','')
  #print(website)
  domains=set()
  website="https://crt.sh/?q=%25"+website
  #print(website)
  req=requests.get(website)
  soup=BeautifulSoup(req.text,features="lxml")
  rows=soup.findAll('td')
  for i in rows:
   if i.text.endswith(".com"):
    domains.add(i.text)
    print(i.text)
    #domains.add(str(i).split('\n')[5].replace('<td>','').replace('</td>',''))
  #print(domains)
  for i in domains:
   req=requests.get("http://"+i)
   if req.status_code==404 or "Not found" in req.text:
    print("subdomain takeover found on domain"+i)
   else:
    print(i)
 except:
  pass

#check_subdomain('http://testphp.vulnweb.com/')
