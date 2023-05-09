import socket


def receive_text_over_ethernet(host, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Bind the socket to the specified host and port
            s.bind((host, port))

            # Listen for incoming connections
            s.listen(1)

            print("Waiting for a connection...")

            # Accept the connection
            conn, addr = s.accept()

            print("Connection established with:", addr)

            # Receive the data
            data = conn.recv(1024).decode()
            print("Received text message:", data)

            # Send a response (optional)
            response = "Message received!"
            conn.sendall(response.encode())

        except socket.error as e:
            print("Socket error:", str(e))
        except Exception as e:
            print("Error:", str(e))


# Specify the host and port to listen on
host = "0.0.0.0"  # Listen on all available network interfaces
port = 1234  # Use the same port number specified in the sending code

# Call the function to start listening for incoming connections
receive_text_over_ethernet(host, port)
