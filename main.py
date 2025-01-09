import socket

host = '192.168.1.100'  # Replace with the device's IP
port = 12345            # Replace with the device's port
buffer_size = 1024

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f"Connected to {host}:{port}")

    # command = "YOUR_COMMAND\n"
    # s.sendall(command.encode())
    # print(f"Command sent: {command}")

    response = s.recv(buffer_size).decode().strip()
    print(f"Device response: {response}")

except socket.error as e:
    print(f"Failed to connect: {e}")

finally:
    s.close()
    print("Connection closed.")
