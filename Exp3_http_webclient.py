import socket
 
# Web server details
host = "example.com"
port = 80
 
# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    # Connect to the web server
    client_socket.connect((host, port))
 
    # Send HTTP GET request
    request = (
        "GET / HTTP/1.1\r\n"
        "Host: example.com\r\n"
        "Connection: close\r\n\r\n"
    )
    client_socket.sendall(request.encode())
 
    # Receive webpage response
    response = b""
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data
 
    # Display the response
    print(response.decode("utf-8", errors="replace"))
 
except socket.error as e:
    print("Error:", e)
 
finally:
    client_socket.close()
