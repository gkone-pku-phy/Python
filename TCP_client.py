import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
# s.send("123".encode("utf-8"))
# print(s.recv(1024).decode("utf-8"))
# s.send("data".encode("utf-8"))
# print(s.recv(1024).decode("utf-8"))
while True:
    data=input()
    s.send(data.encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))