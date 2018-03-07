import math
import urllib
from netaddr import IPSet, IPNetwork, cidr_merge
opener = urllib.FancyURLopener()
f = opener.open("ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest")
lines=f.readlines()

ip_list =[]
for line in lines:
          if (('ipv4' in line) & ('TR' in line)):
          s=line.split("|")
          net=s[3]
          cidr=float(s[4])
          ip = "%s/%d" % (net,(32-math.log(cidr,2)))
          ip_list.append(IPNetwork(ip))
cidr_merge(ip_list)
for ip_network in ip_list:
    print str(ip_network)
