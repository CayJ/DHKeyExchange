import hashlib
import random
from crypto import encryption, decryption

class Person:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.private_key = random.randint(1, p)
        self.public_key = pow(g, self.private_key, p)
    
    def compute_shared_secret(self, other_public_key):
        return pow(other_public_key, self.private_key, self.p)

    # derive a symmetric encryption key from the shared secret, first 16 bytes of a SHA256 hash
    def compute_shared_key(self, shared_secret):
        return hashlib.sha256(str(shared_secret).encode()).digest()
    
    def encrypt_message(self, message, key):
        return encryption(message, key)

    def decrypt_message(self, ciphertext, key):
        return decryption(ciphertext, key)
