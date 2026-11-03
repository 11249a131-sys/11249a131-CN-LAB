import socket
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12346))
server.listen(1)
 
print("Chat Server is waiting for a client...")
 
conn, addr = server.accept()
print("Client connected:", addr)
print("Type 'exit' to close the chat.")
 
while True:
    message = conn.recv(1024).decode()
 
    if not message or message.lower() == "exit":
        print("Client disconnected.")
        break
 
    print("Client:", message)
 
    reply = input("You: ")
    conn.sendall(reply.encode())
 
    if reply.lower() == "exit":
        break
 
conn.close()
server.close()
print("Chat Server closed.")
exp5_chat_client.py
import socket
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12346))
 
print("Connected to Chat Server!")
print("Type 'exit' to close the chat.")
 
while True:
    message = input("You: ")
    client.sendall(message.encode())
 
    if message.lower() == "exit":
        break
 
    reply = client.recv(1024).decode()
 
    if not reply or reply.lower() == "exit":
        print("Server disconnected.")
        break
 
    print("Server:", reply)
 
client.close()
print("Chat Client closed.")
