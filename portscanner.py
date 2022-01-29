import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
from colorama import init

colorama.init()

target = input("Enter de URL/IP to Scan\n>")

def scanner(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((target, port))
        scanner.close()
        print(f'[{Fore.GREEN}+{Fore.RESET}] {port} is Open')
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1024):
        executor.submit(scanner, target, port)