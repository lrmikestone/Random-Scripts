import socket
import paramiko
import os
from termcolor import colored

window_width = os.get_terminal_size().columns
width = window_width - 5

def clear_screen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def check_sftp_accessibility(server, port):
    try:
        transport = paramiko.Transport((server, port))
        transport.connect()
        transport.close()
        return True
    except (paramiko.SSHException, socket.error) as e:
        return False

def main():
    with open('servers.txt', 'r') as file:
        lines = file.readlines()
    clear_screen()
    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            server, port = line.split(':')
            port = int(port)
        except ValueError:
            print(f"Something is up with your file: {line}")
            continue

        is_accessible = check_sftp_accessibility(server, port)
        status = colored("[OK]", "green") if is_accessible else colored("[FAIL]", "red")
        server_deets = str(server) + ":" + str(port)
        results.append(f"{server_deets:<{width - len(status)}}{status}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
