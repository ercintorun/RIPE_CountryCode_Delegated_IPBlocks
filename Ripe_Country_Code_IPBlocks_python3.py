import math
import urllib
from netaddr import IPSet, IPNetwork, cidr_merge
import requests
import urllib.request
country_code="TR"

download_url = "ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest"
with urllib.request.urlopen(download_url) as r:
    data = r.readlines()

data_list=[]
for item in data: 
	data_list.append(item.decode("utf-8"))

ip_list =[]
for line in data_list:
	if (('ipv4' in line) & (country_code in line)):
			s=line.split("|")
			net=s[3]
			cidr=float(s[4])
			ip = "%s/%d" % (net,(32-math.log(cidr,2)))
			ip_list.append(IPNetwork(ip))
cidr_merge(ip_list)
for ip_network in ip_list:
	print (str(ip_network))