import requests
import sys
import json


def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=json&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    results = r.json()
    return results[1:]



def domains(host,with_subs):
    if host.startswith('https://'):
        host=host.replace("https://",'')
    elif host.startswith("http://"):
        host=host.replace("http://",'')
    host=host.split("/")[0]
    urls = waybackurls(host, with_subs)
    json_urls = json.dumps(urls)
    #print(with_subs)
    if urls:
        for i in urls:
            
            i[0]=i[0].replace(":80",'')
            print(i[0])
            with open("demofile.txt", 'a') as f:
                f.write(i[0]+'\n')
        #
        #filename = '%s-waybackurls.json' % host
        #with open(filename, 'w') as f:
        #   f.write(json_urls)
        #print('[*] Saved results to %s' % filename)
    else:
        print('[-] Found nothing')

#domains("http://testhtml5.vulnweb.com",False)