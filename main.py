import socket
import threading
import time
import pickle
import rsa

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12346

name = input("İsminizi Girin : ")
(public_key, private_key ) = rsa.newkeys(1024)
msg=pickle.dumps(public_key)


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen()
print(f"Program {SERVER_ADDRESS}:{SERVER_PORT} adresinden dinleniyor...")
print("\n")

conn, addr = server.accept()

def send():
  while True:
    message = input("")
    encrypted_message = rsa.encrypt(message.encode(), pkey)
    conn.send(encrypted_message)


def recv():
  while True:
    try:
      message = conn.recv(1024)
      decrypted_message = rsa.decrypt(message, private_key).decode()
      print(f"{name_agent}: " +decrypted_message)

    except Exception as err:
      print(f"Error is {err}")
      conn.close()
      break
      
conn.send(str.encode(name))
name_agent=conn.recv(1024).decode() 
conn.send(msg) 
rmsg = conn.recv(1024) 
pkey = pickle.loads(rmsg) 

threading.Thread(target=send).start()
threading.Thread(target=recv).start()