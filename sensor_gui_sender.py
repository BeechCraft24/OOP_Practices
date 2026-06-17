import json
import socket
import tkinter as tk
from tkinter import messagebox

FILE_PATH = r"F:\OOP\json_files2\sensor_data.json"
HOST = "192.168.12.224"   
PORT = 5000

def save_json():
    try:
        sensor_data = {
            "voltage": float(voltage_entry.get()),
            "current": float(current_entry.get()),
            "temperature": float(temperature_entry.get())
        }

        with open(FILE_PATH, "w") as file:
            json.dump(sensor_data, file, indent=4)

        messagebox.showinfo("Success", "JSON file created/updated")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def send_file():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))

            with open(FILE_PATH, "rb") as file:
                client.sendall(file.read())

        messagebox.showinfo("Success", "Sensor data sent to Kali")

    except FileNotFoundError:
        messagebox.showerror("File Error", "JSON file not found. Click Save JSON first")

    except ConnectionRefusedError:
        messagebox.showerror("Connection Error", "Kali receiver is not running")

    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Sensor Data Editor - Windows")

tk.Label(window, text="Voltage").grid(row=0, column=0, padx=10, pady=10)
voltage_entry = tk.Entry(window)
voltage_entry.grid(row=0, column=1)

tk.Label(window, text="Current").grid(row=1, column=0, padx=10, pady=10)
current_entry = tk.Entry(window)
current_entry.grid(row=1, column=1)

tk.Label(window, text="Temperature").grid(row=2, column=0, padx=10, pady=10)
temperature_entry = tk.Entry(window)
temperature_entry.grid(row=2, column=1)

save_button = tk.Button(window, text="Save JSON", command=save_json)
save_button.grid(row=3, column=0, columnspan=2, pady=15)

send_button = tk.Button(window, text="Send to Kali", command=send_file)
send_button.grid(row=4, column=0, columnspan=2, pady=15)

window.mainloop()