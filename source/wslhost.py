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

def run(hp: str, bn: str):
    path = hp
    bn = bn
    #os.chmod(path, stat.S_IRWXO)
    try:
        with open(path, "r") as f:
            lines = f.readlines()
        with open(path, "w") as f:
            max = len(lines)-1
            for line in range(len(lines)):
                if bn not in lines[line].strip("\n"):
                    f.write(lines[line])
                    if line == max:
                        if '\n' not in lines[line]:
                            print(lines[line])
                            f.write('\n')
            f.close()

        wslip = f"{get_ip_address()} {bn}"

        with open(path, "a") as f:
            f.write(f'{wslip}')
            logger.info(f"'{wslip}' appended to :\n{path}")
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

    parser.add_argument(
        '--bn',
        type=str,
        help='Bash name',
        required=True
    )
    args = parser.parse_args()

    #logger.info(f"Args: {args}")

    run(args.hp, args.bn)
