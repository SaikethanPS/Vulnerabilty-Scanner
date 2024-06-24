import requests
from bs4 import BeautifulSoup

form_urls=set()
form_name=set()

def unique_forms(form,url):
 if form.has_attr('name'):
  form_name.add(form['name'])
  form_urls.add(url)
 elif form.has_attr('id'):
  form_name.add(form['id'])
  form_urls.add(url)
 elif form.has_attr('action') and form.has_attr('method'):
  form_name.add(form['action']+form['method'])
  form_urls.add(url)
 else:
  pass
  
  
   
  
def check_if_form(url):
 try:
  request=requests.get(url)
  parseHtml=BeautifulSoup(request.text, 'html.parser')
  forms=parseHtml.find_all('form')
  #print(forms)
  for form in forms:
   if form is not None :
    unique_forms(form,url)
 
 except:
   pass


def iterate_through_file(filename):
 f=open(filename)
 lines=f.read().split("\n")
 f.close()
 for i in lines:
  check_if_form(i)
  #print(i)
 return form_urls

#print(iterate_through_file('demofile.txt'))




 


