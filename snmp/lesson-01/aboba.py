import os
import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-o','--oids')
args = parser.parse_args(sys.argv[1:])

command = 'snmpwalk -v 2c -c sirius 192.168.254.18 .'
with open ('snmp.txt','w') as file:
    c = subprocess.getoutput(command)
    file.write(c)

print(c)

# def aboba(n):
#     command = 'snmpwalk -v 2c -c sirius 192.168.254.18 ' + n
#     filename = n + '.txt'
#     with open (filename,'w') as file:
#         c = subprocess.getoutput(command)
#         file.write(c)

# aboba(args.oids)