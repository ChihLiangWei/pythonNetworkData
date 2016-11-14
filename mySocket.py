import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('python-data.dr-chuck.net', 80) )

mysock.send('GET http://python-data.dr-chuck.net/regex_sum_42.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
mysock.close()
