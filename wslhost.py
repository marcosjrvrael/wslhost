 # -*- coding: UTF8 -*-
import os
import sys
import socket

def get_ip_address(): -> String
    ''' 
        Function responsable to return current ipAdress of eth0 ethernet interface
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

path = "/mnt/c/Windows/System32/drivers/etc/hosts"

try:
    with open(path, "r") as f:
        lines = f.readlines()
    with open(path, "w") as f:
        for line in lines:
            if "wsl.local" not in line.strip("\n"):
                f.write(line)

    wslip = f"{get_ip_address()} wsl.local"

    with open(path, "a") as f:
        f.write(wslip)
        print(f"'{get_ip_address()} wsl.local' appended to :\n{path}")
except e:
    raise Exception(f"{e}")