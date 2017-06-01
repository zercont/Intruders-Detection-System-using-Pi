s = socket.socket()         # Create a socket object
host = "192.168.43.225" # Get local machine name
port = 8000               # port

s.connect((host, port))
s.send('10')
s.close  
