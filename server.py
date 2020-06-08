import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 8088))
print('Binded UDP to 8088 port')
data, addr = s.recvfrom(1024)
data = float(data)*1.8 + 32
send_data = 'after conversion, temp (unit: Fa Celsius) : ' + str(data)
print('Received from %s:%s.' % addr)
s.sendto(send_data.encode(), addr)
s.close()
