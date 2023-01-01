import rsa
import hashlib
from cryptography.fernet import Fernet
import math
import random
import socket
import threading
def take_personID():
 with open("ID.txt","r",encoding="utf8") as file:
    ID_elements = file.read().split("\n")
    userIDList = []

    for i in range(0,len(ID_elements)):
        userIDList.append(ID_elements[i].split(" ")[1])

    userID = userIDList[1]
 return userID

def generate_sessionKey():
    session_key = Fernet.generate_key()
    return session_key

def generate_Keys_src():
    src_publicKey,src_privateKey = rsa.newkeys(1024)
    with open('src_pubkey.pem','wb') as f:
        f.write(src_publicKey.save_pkcs1('PEM'))
    with open('src_privkey.pem','wb') as f:
        f.write(src_privateKey.save_pkcs1('PEM'))
        
    


def generate_Keys_dst():
    dst_publicKey,dst_privateKey = rsa.newkeys(1024)
    with open('dst_pubkey.pem','wb') as f:
        f.write(dst_publicKey.save_pkcs1('PEM'))
    with open('dst_privkey.pem','wb') as f:
        f.write(dst_privateKey.save_pkcs1('PEM'))  

def load_keys_dst():
      with open('dst_pubkey.pem','rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
      with open('dst_privkey.pem','rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
      return publicKey,privateKey

def load_keys_src():
      with open('src_pubkey.pem','rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())
      with open('src_privkey.pem','rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
      return publicKey,privateKey

def encrypt(message,public_key):
     
     
        
     encrypted_msg = rsa.encrypt(str(message).encode(),public_key)
     return encrypted_msg

def decrypt(cipher_text,key):
  return rsa.decrypt(cipher_text,key)

def sign(message,src_private_key):
    signature = rsa.sign(str(message).encode('ascii'),src_private_key,'SHA-256')
    return signature

def verify(message,signature,public_key):
    return rsa.verify(str(message).encode(),signature,public_key)

generate_Keys_src()
generate_Keys_dst()
load_keys_src()
src_pub, src_priv = load_keys_src()
dst_pub,dst_priv = load_keys_dst()
encrypted = encrypt(take_personID(),dst_pub)
decrypted = decrypt(encrypted,dst_priv)


#print(decrypted)
signed = sign(take_personID(),src_priv)
signed2 = sign(encrypted,src_priv)
verified2 = verify(encrypted,signed2,src_pub)
#encrypted = encrypt(signed,dst_pub)

verified = verify(take_personID(),signed,src_pub)

if verified2:
    print("Authentication is correct")
def hashing(ID):

    ID = str(ID)
    hash_object = hashlib.sha256(ID.encode())
    hashedID = hash_object.hexdigest()
    return hashedID
