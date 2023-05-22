import socket
import threading
import time
import pickle
import rsa

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12346

name=input("İsminizi Girin : ")
print("\n")
(public_key, private_key) = rsa.newkeys(1024)
msg = pickle.dumps(public_key)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))


def send():
  while True:
    message = input("")
    encrypted_message = rsa.encrypt(message.encode(), pkey)
    client.send(encrypted_message)


def recv():
  while True:
    try:
      message = client.recv(1024)
      decrypted_message = rsa.decrypt(message, private_key).decode()
      print(f"{name_agent}: " + decrypted_message)

    except Exception as err:
      print(f"Error is {err}")
      client.close()
      break

name_agent=client.recv(1024).decode() 
client.send(str.encode(name))
rmsg=client.recv(1024)
pkey=pickle.loads(rmsg) 
client.send(msg)

threading.Thread(target=send).start()
threading.Thread(target=recv).start()
