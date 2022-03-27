"""nmap is not part of the python standard library so you'll have to install it using:
pip3 or pip install python-nmap or visit nmap.org and download one for your operating system
This script takes an IP address and scan for ports 21, 22, 80, 139, 443"""

import nmap
import sys

#the target variable takes the command line argument
target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443]

scan_v = nmap.PortScanner()
print("\n Scanning ", target, " for ports 21, 22, 80, 443...\n")

for port in ports:
    portscan = scan_v.scan(target, str(port))
    print("Port ",port, " is ", portscan["scan"][target]["tcp"][port]['state'])

print("\nHost ", target, " is ", portscan['scan'][target]['state']['status'])