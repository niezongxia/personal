#mac.py


'''
def get_mac_address():
    import uuid
    node=uuid.getnode()
    mac=uuid.UUID(int=node).hex[-12:]
    return mac
print(get_mac_address())
'''
##def get_mac_address():
##    import os
##    import sys
##    mac=None
##    if sys.platform=="win64":
##        for line in os.popen("nbtstat -A 22.11.236.24"):
##            print(line)
##            if line.lstrip().startswith("MAC 地址"):
##                mac=line.split(":")[1].strip().replace("-",":")
##                break
##    else:
##        for line in os.popen("/sbin/ifconfig"):
##            if 'Enter' in line:
##                mac=line.split()[4]
##                break
##    return mac
##get_mac_address()
##    else:
##        print("失败")

##import os
##def get_dstmac(dstip):
##    s='ping '+dstip
##    os.popen(s)
##    for line in os.popen("arp -a"):
##        if line.lstrip().startswith(dstip):
##            s1=line.split()
##            mac=s1[1].replace("-",":")
##            print(mac)
##
##get_dstmac("22.11.236.164")

import os
import sys
def get_dstmac(dstip):
##    s='ping '+dstip
##    os.popen(s)
    for line in os.popen("cmd /c C:/Windows/sysnative/nbtstat.exe -a "+dstip):
        if line.lstrip().startswith("MAC 地址 ="):
            s1=line.split()
            mac=s1[3].replace("-",":")
            print(mac)
        
get_dstmac(sys.argv[1])
