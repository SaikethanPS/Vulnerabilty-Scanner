import requests
from form_urls import *
from bs4 import BeautifulSoup
import chk

def check_host(website):
 list_of_urls=iterate_through_file('demofile.txt')
 for url in list_of_urls:
  try:
   req=requests.get(url,headers={'Host':'www.bing.com'})
   if req.status_code==302 or req.status_code==301 or 'www.bing.com' in req.text:
    print('Host header injection found on '+website)

   req=requests.get(url,headers={'X-Forwarded-Host':'www.bing.com'})
   if req.status_code==302 or req.status_code==301 or 'www.bing.com' in req.text:
    print('Host header injection found on '+website)
  except:
   pass

def check_host(url,cookie):
 #list_of_urls=iterate_through_file('demofile.txt')
 #for url in list_of_urls:
 try:
  req=requests.get(url,headers={'Host':'www.bing.com'},cookies=cookie)
  #print(req.url)
  if req.status_code==302 or req.status_code==301 or 'www.bing.com' in req.text:
   print('Host header injection found on '+url)

  req=requests.get(url,headers={'X-Forwarded-Host':'www.bing.com'},cookies=cookie)
  if req.status_code==302 or req.status_code==301 or 'www.bing.com' in req.text:
   print('Host header injection found on '+url)
 except:
  pass


#check_host('http://localhost/bWAPP/hostheader_1.php',chk.getCookie("security_level=0; PHPSESSID=7vchipu70lrkvo2abd3297jva4"))
