import socket
import write
def server_start():
    server_ip = socket.gethostbyname(socket.gethostname()) #get your ip
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind((server_ip, 52001)) #build server in this port
    tcp_server.listen(1)
    print('Wait tcp accepting...')
    client, address = tcp_server.accept() #accept  connect in client
    print('Connected client ip : {}'.format(address))
    while True: #loop
        try:
            rcv_data = client.recv(1024)#client message recieve
            write.write_data(rcv_data,rcv_data.decode("utf-8")) #move write_data() to rcv_data and decode data
            print('Data : {}'.format(rcv_data.decode("utf-8")))#display
        except KeyboardInterrupt as e:
            client.close()
            exit()
            

if __name__ == "__main__":
    server_start()#main value
