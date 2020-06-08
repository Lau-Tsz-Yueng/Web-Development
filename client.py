import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('please input the Celsius degree: unit conversion')
s.sendto(data.encode(), ('0.0.0.0', 8088))
print(s.recv(1024).decode())
s.close()