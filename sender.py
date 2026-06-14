import socket

HOST = "192.168.12.224"
PORT = 5000

file_path = r"F:\OOP\json_files\sensor_data.json"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.connect((HOST, PORT))

    with open(file_path, "rb") as file:
        client.sendall(file.read())

print("File sent.")