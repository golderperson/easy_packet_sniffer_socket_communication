import socket
import propcap
def client_start():
    ip_address = socket.gethostbyname(socket.gethostname())#server ip 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((str(ip_address), 52001))#connect server 
    while True:
        c=propcap.pcap()#move pcap() in propcap
        tcp_socket.send(c.encode("utf-8"))#send c

if __name__ == "__main__":
    client_start()#main value
