import socket

username = "sophie"
password = "asdfawg"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

msg = client.recv(1024).decode()
print(msg)
client.send(username.encode())
msg = client.recv(1024).decode()
print(msg)
client.send(password.encode())

print(client.recv(1024).decode())
    