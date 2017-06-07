import socket, thread

status = 'offline'


def server(port=4050):

    try:
        host = (
            [l for l in
             ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
              [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
    except:
        host = '127.0.0.1'
        print 'no internet connection found, server will start on localhost.'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind((host, port))
        print "starting server on %s:%s" % (host, port)
        status = 'online'
    except:
        print 'port is already in use'
        if status is not 'online':
            status = 'offline'

    sock.listen(2)
    sock_list = []

    def broadcast(sock, message, addr, flags):
        for socket in sock_list:
            # sends everyone except the current socket.
            if socket != sock:
                if 'chat' in flags:
                    socket.send(message)
                elif not len(flags):
                    pass

    def new_socket(clientsock, addr):
        try:
            while True:
                data = clientsock.recv(1024)
                if not data or data == "!quit":
                    break
                else:
                    broadcast(clientsock, data, addr, ['chat'])
        except Exception:
            print Exception

        clientsock.close()
        sock_list.remove(clientsock)

        try:
            print 'disconnected from ', addr

        except:
            pass

    while True:
        nsock, addr = sock.accept()
        sock_list.append(nsock)
        print 'connected from', addr
        sock_list[0].send('-1')
        thread.start_new_thread(new_socket, (nsock, addr))

    sock.close()
