from asyncore import read
import os
import time
in_1 = []
in_2 = []
Out_1 = []
Out_2 = []
time_start = time.time()
time_stop = 0
while time_stop - time_start < 100:

    command = 'snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::if'
    in_1.append(int((os.popen('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifInOctets.1')).read().split(':')[-1]))
    in_2.append(int((os.popen('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifInOctets.2')).read().split(':')[-1]))
    Out_1.append(int((os.popen('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifOutOctets.1')).read().split(':')[-1]))
    Out_2.append(int((os.popen('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifOutOctets.2')).read().split(':')[-1]))
    time_stop = time.time()
print(in_1)

    # res = str(b)
    # print(res)
    # os.system('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifInOctets.2')
    # os.system('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifOutOctets.1')
    # os.system('snmpget -v 2c -c sirius 176.208.128.14 IF-MIB::ifOutOctets.2')
    #print(b)
    #time.sleep(20)

