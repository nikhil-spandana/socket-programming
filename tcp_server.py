import socket

def connect_hardware(device_ip: str, device_port: int, ping_message: str, buffer_size: int, timeout: int) -> None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
            tcp_socket.settimeout(timeout)
            print(f"Connecting to {device_ip}:{device_port} via TCP...")

            tcp_socket.connect((device_ip, device_port))
            print("Connection established.")

            tcp_socket.sendall(ping_message.encode())
            print(f"Sent: {ping_message}")

            response = tcp_socket.recv(buffer_size).decode().strip()
            print(f"Received response: {response}")

    except socket.timeout:
        print(f"No response received within {timeout} seconds. Device may be unreachable.")

    except socket.error as e:
        print(f"Socket error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    device_ip = '192.168.1.100'
    device_port = 12345
    ping_message = "PING"
    buffer_size = 1024
    timeout = 5

    connect_hardware(device_ip, device_port, ping_message, buffer_size, timeout)
