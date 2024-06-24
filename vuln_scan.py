import subdomain_takeover
import check_ssrf
import check_sql
import sensitive_data
import xss_check
import check_host_header
import cors
import secrity_header
import check_xxe
#import scrapping
import scraping
import os
from termcolor import colored
import sys
import scrap
import waybackurls
import chk

#domain=''
def printBanner():
 cmd="figlet -w 100 'Crawler'"
 returned_value=os.system(cmd)

#printBanner()

def crawler():
 try:
  if str(sys.argv[3])!='':
    pass
   #domain=sys.argv[1]
   #print(domain)
 except:
  printBanner()
  try:
  #print(sys.argv[2])
  #print(chk.getCookie(sys.argv[2]))
  #print(colored('Checking as Authenticated User','green'))
   scrap.crawler(sys.argv[1],'demofile.txt','',chk.getCookie(sys.argv[2]))
   
   waybackurls.domains(sys.argv[1],False)
  except:
   print(colored('Checking as Unauthenticated User','red'))
   scraping.crawler(sys.argv[1], 'demofile.txt', '')
   waybackurls.domains(sys.argv[1],False)
  


def printBanner1():
 cmd="figlet -w 100 'Vulnerability Scanner'"
 returned_value=os.system(cmd)

printBanner1()

crawler()

def select(a):
	

 if a==1:
  print(colored('Checking XSS','green'))
  try:
   if str(sys.argv[3]) != '':
    #print(domain)
    xss_check.xsssC(sys.argv[1],chk.getCookie(sys.argv[2]))
    #return
  except:
   try:
    #print("jhjh")
    xss_check.xsssC(chk.getCookie(sys.argv[2]))
   #menu()
    #return 
   except:
    xss_check.xsss()
  menu()
  return 

 elif a==2:
  print(colored('Checking SQL Injection','green'))
  try:
   if str(sys.argv[3]) != '':
    check_sql.sqliC(sys.argv[1],chk.getCookie(sys.argv[2]))
    
  except:
   try:
    check_sql.sqliC(chk.getCookie(sys.argv[2]))
   except:
    check_sql.sqli()
  menu()
  return

 elif a==3:
  print(colored('Checking XXE','green'))
  try:
   if str(sys.argv[3]) != '':
    check_xxe.xxeC(sys.argv[1],chk.getCookie(sys.argv[2]))
    #return
  except:
   try:
    check_xxe.xxeC(chk.getCookie(sys.argv[2]))
   except:
    check_xxe.xxe()
  menu()
  return 
 elif a==4:
  print(colored('Checking SSRF','green'))
  try:
   if str(sys.argv[3]) != '':
    check_ssrf.ssrfC(sys.argv[1],chk.getCookie(sys.argv[2]))
    #return
  except:
   try:
    check_ssrf.ssrfC(chk.getCookie(sys.argv[2]))
   except:  
    check_ssrf.ssrf()
  menu()
  return 
 elif a==5:
  print(colored('Checking CORS','green'))
  try:
    if str(sys.argv[3])!='':
      cors.check_cors(sys.argv[1],chk.getCookie(sys.argv[2]))
  except:
    cors.check_cors()
  menu()
  return 
 elif a==6:
  print(colored('Checking Missing Security Headers ','green'))
  secrity_header.check_secruity_headers(sys.argv[1])
  menu()
  return 
 elif a==7:
  print(colored('Checking subdomain_takeover ','green'))
  subdomain_takeover.check_subdomain(sys.argv[1])
  menu()
  return 
 elif a==8:
  print(colored('Checking Sensitive Data Leak ','green'))
  sensitive_data.check_sensitive(sys.argv[1])
  menu()
  return 
 elif a==9:
  print(colored('Checking Host Header Injection ','green'))
  try:
   if str(sys.argv[3])!='':
    check_host_header.check_host(sys.argv[1],chk.getCookie(sys.argv[2]))
  except: 
   check_host_header.check_host(sys.argv[1])
  menu()
  return 
 elif a==0:
  print(colored('Exiting  ','red'))
  sys.exit()
 

def menu():
 print()
 print(colored('1. XSS ','blue'))
 print(colored('2. SQL Injection ','blue'))
 print(colored('3. XXE ','blue'))
 print(colored('4. SSRF ','blue'))
 print(colored('5. CORS ','blue'))
 print(colored('6. Missing Security Headers ','blue'))
 print(colored('7. subdomain_takeover ','blue'))
 print(colored('8. Sensitive Data Leak ','blue'))
 print(colored('9. Host Header Injection ','blue'))
 print(colored('0. Exit ','red'))
 print()
 print(colored('Enter your choice','green'))
 try:
  a=int(input())
  select(a)
 except:
  print(colored('Enter correct option','blue'))
  sys.exit()

menu()
