import socket

def send_text_over_ethernet(text, host, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to the specified host and port
            s.connect((host, port))
            
            # Send the text message
            s.sendall(text.encode())
            
            # Wait for the server's response (optional)
            response = s.recv(1024)
            print("Server's response:", response.decode())
            
        except socket.error as e:
            print("Socket error:", str(e))
        except Exception as e:
            print("Error:", str(e))

# Specify the host and port for the connection
host = '192.168.1.225'  # Replace with the IP address of the receiving device
port = 1235  # Replace with the desired port number

# Specify the text message to send
text_message = "Send nudes"

# Call the function to send the text message


def main():
    
    # Call the function to send the message
    send_text_over_ethernet(text_message, host, port)

if __name__ == '__main__':
    print("test")
    main()


