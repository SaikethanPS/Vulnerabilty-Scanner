import requests
from bs4 import BeautifulSoup
import mechanize
from form_urls import *
from form_input import *
import chk


def make_req(data,payloa):
 d={}
 for i in data:
  d[i]=payloa
 return d

def checkSqlInjection(res,f,error):
 flag=False
 for i in error:
  if i in res.text and bool(f):
   print('Sql injection Found on url:'+res.url)
   print('payload:'+str(f))
   flag=True
   break
 return flag

def sqli():
 payload=['\'','"','\\']
 error=['error','exception','illegal','invalid','fail','stack','access','directory','file','not found','varchar','ODBC','SQL','SELECT']
 list_of_urls=iterate_through_file('demofile.txt')

 for i in list_of_urls:
  input_req=return_input(i,'')
  for k in range(0,len(input_req),3):
   if input_req[k+1]=='post' or input_req[k+1]=='POST':
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.post(input_req[k],d)
     if checkSqlInjection(request,d,error):
      break
   elif input_req[k+1]=='get' or input_req[k+1]=='GET':
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.get(input_req[k],d)
     if checkSqlInjection(request,d,error):
      break

def sqliC(cookie):
 payload=['\'','"','\\']
 error=['error','exception','illegal','invalid','fail','stack','access','directory','file','not found','varchar','ODBC','SQL','SELECT']
 list_of_urls=iterate_through_file('demofile.txt')

 for i in list_of_urls:
  input_req=return_input(i,cookie)
  for k in range(0,len(input_req),3):
   if input_req[k+1]=='post' or input_req[k+1]=='POST':
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.post(input_req[k],d,cookies=cookie)
     if checkSqlInjection(request,d,error):
      break
   elif input_req[k+1]=='get' or input_req[k+1]=='GET':
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.get(input_req[k],d,cookies=cookie)
     if checkSqlInjection(request,d,error):
      break

def sqliC(url,cookie):
 payload=['\'','"','\\']
 #print("h1")
 error=['error','exception','illegal','invalid','fail','stack','access','directory','file','not found','varchar','ODBC','SQL','SELECT']
 #list_of_urls=iterate_through_file('demofile.txt')

 #for i in list_of_urls:
 input_req=return_input(url,cookie)
 #print(input_req)
 for k in range(0,len(input_req),3):
  if input_req[k+1]=='post' or input_req[k+1]=='POST':
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.post(input_req[k],d,cookies=cookie)
    if checkSqlInjection(request,d,error):
     break
  elif input_req[k+1]=='get' or input_req[k+1]=='GET':
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.get(input_req[k],d,cookies=cookie)
    if checkSqlInjection(request,d,error):
     break

#sqliC("http://localhost/bWAPP/sqli_6.php",chk.getCookie("security_level=0; PHPSESSID=htlvtb5uhmphoiup6ojb608f4o"))
