import sys

def getCookie(ck):
 #ck=sys.argv[1]
 cks=ck.split(';')
 cookie={}
 for i in cks:
  param=i.split('=')[0].strip()
  value=i.replace(param+'=','').strip()
  if value.endswith('='):
  	value="\""+value+"\""
  cookie[param]=value
 return cookie
#getCookie(sys.argv[1])
#ck1,ck2=ck.split(';')[0],ck.split(';')[1]
#ck2=ck.split(';')[1]
#print(ck1.split('='),ck2.replace(ck2.split("=")[0]+'=',''))
