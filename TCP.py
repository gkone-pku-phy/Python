#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
#所以，我们要创建一个基于TCP连接的Socket，可以这样做：
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.baidu.com',80))
#创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
#客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，但是怎么知道新浪服务器的端口号呢？
#答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
#注意参数是一个tuple，包含地址和端口号。

#建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容：
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com.cn\r\nConnection:close\r\n\r\n')
buffer = []
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
print(data)
s.close()
header , html=data.split(b'\r\n\r\n',1)
#print("after split:\n\nheader:{%s}\nhtml:{%s}".format(header,html))
print(header.decode('utf-8'))
with open('baidu.html','wb') as f:
    f.write(html)
