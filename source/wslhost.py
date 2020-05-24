 # -*- coding: UTF8 -*-
import os
import sys
import stat
import socket
import logging
import argparse

logging.info('')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_ip_address() -> str:
    ''' 
        Function responsable to return current ipAdress of eth0 ethernet interface
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def run(hp: str):
    path = hp
    os.chmod(path, stat.S_IRWXO)
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
            logger.info(f"'{get_ip_address()} wsl.local' appended to :\n{path}")
    except Exception as e:
        logger.info(f'{e}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Getting parameters'
    )
    parser.add_argument(
        '--hp',
        type=str,
        help='Path to hosts file',
        required=True
    )
    args = parser.parse_args()

    #logger.info(f"Args: {args}")

    run(args.hp)
