#!/usr/bin/env python3
import time
import re
import subprocess
import json

nodes = {}

output = subprocess.check_output(["alfred-json","-r","158","-f","json","-z"])
data = json.loads(output.decode("utf-8"))

for mac, node in data.items():

    try:
        hostname = re.sub(r'[^a-z0-9\-]',"", node["hostname"].lower()) 
        for address in node["network"]["addresses"]:
            if address.startswith("fd00"):
                nodes[hostname] = address
    except: 
        pass


print("$ORIGIN nodes.fffd.")
print("$TTL 3600	; 1 Stunde")
print("@			IN 	SOA	ns.fffd. hostmaster.fffd. (")
print("					" + str(int(time.time())) + "; serial")
print("					86400	; refresh")
print("					7200	; retry")
print("					3600000	; expire")
print("					7200	; TTL")
print("					)")
print("")
print("")
print("@			IN	NS	ns0.fffd.")
print("@			IN	NS	ns1.fffd.")
print("@			IN	NS	ns2.fffd.")
print("@			IN	NS	ns3.fffd.")
print("")
print("")


for hostname in nodes.keys():
    print(hostname + "		IN	AAAA	" + nodes[hostname])
    print("")

print("")

