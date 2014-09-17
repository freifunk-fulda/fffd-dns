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
        nodes[hostname] = node["network"]["addresses"][0]
    except: 
        pass


print("$ORIGIN nodes.fffd.")
print("$TTL 3600	; 1 Stunde")
print("@			IN 	SOA	localhost. hostmaster.freifunk-fulda.de. (")
print("					" + time.strftime("%Y%m%d%S") + "; serial")
print("					86400	; refresh")
print("					7200	; retry")
print("					3600000	; expire")
print("					172800	; TTL")
print("					)")
print("")
print("")
print("@			IN	NS	localhost.")
print("")
print("")


for hostname in nodes.keys():
    print(hostname + "		IN	AAAA	" + nodes[hostname])
    print("")

print("")

