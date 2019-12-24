import requests
import sys
if len(sys.argv)==3:
    pass
else:
    print "you missed something here check the apikey or the domain name"
    print sys.argv[0]+" apikey domain_name"
    print sys.argv[0]+" xxxxxx xyz.com"
    exit()
url='https://www.virustotal.com/vtapi/v2/domain/report?apikey=%s&domain=%s' % (sys.argv[1],sys.argv[2])
req=requests.get(url).json()
domainlist=req.get('subdomains')
print str(len(domainlist))+" subdomains found\n"
for i in domainlist:
    print str(i)
#short and sweet script for basic subdomain gathering
