import socket
import time

# list most popular ports
host = "192.168.0.102"
port_list = [
    7, 20, 21, 22, 23, 25,
    53, 69, 80, 88, 102, 110,
    135, 139, 143, 381, 383,
    443, 464, 465, 587, 593,
    636, 691, 902, 989, 990,
    993, 995, 1025, 1194, 1337
]

for port in port_list:
    try:
        # Create socket TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_adress = (host, port)

        # Connect to the server
        client_socket.settimeout(1)
        client_socket.connect(server_adress)
        print(f"[+] {port} open {client_socket.recv(1024)}\n")

    except:
        print(f"[-] {port} close or filter\n")
    
    finally:
        client_socket.close()