from bluetooth import * 
import os

nearby_devices = discover_devices()
file_name = raw_input("enter the name of file to share: ")

for bdaddr in nearby_devices:
    print lookup_name(bdaddr)
    print "address: ",bdaddr
    cmd = "bluetooth-sendto --device=" + bdaddr + " " + file_name
    print cmd
    os.system(cmd)
    
