import requests
from bs4 import BeautifulSoup

def normal_response(website):
	 req=requests.get(website)
	 return len(req.text)

def check_sensitive(website):
 try:
  length_res=normal_response(website)
  if website[:-1]=='/':
   website=website.replace('/','') 
  f=open('file.txt','r')
  for i in f:
  	req=requests.get(website+i)
  	if req.status_code!=404 or req.status_code!=301 or len(req.text)!=length_res:
  		print('Sensitive data found at:'+website+i)
 except:
  pass


#check_sensitive('http://testphp.vulnweb.com/')