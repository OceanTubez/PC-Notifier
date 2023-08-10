import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("PiName / IP Address", 5000))

while True:
        msg = socket.recv(1024).decode("utf-8")
        
        if msg == "alert":
                
                with open("SendToast.py") as f:

                                exec(f.read())
