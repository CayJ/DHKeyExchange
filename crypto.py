import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encryption(message, key):
    # generate an initialization vector
    # backend in Cipher() is automatically set to default
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return iv + encrypted_message

def decryption(ciphertext, key):
    # extract the initialization vector from the ciphertext
    # backend in Cipher() is automatically set to default
    iv, ciphertext = ciphertext[:16], ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    unpadder = padding.PKCS7(128).unpadder()
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(ciphertext) + decryptor.finalize()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message.decode()
