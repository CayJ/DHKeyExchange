from person import Person
from generate_prime import generate_large_prime

p = generate_large_prime(512)  # generate a large prime number
g = 2  # base

print('Generated large prime: ', p)

alice = Person(p, g)
bob = Person(p, g)

print('\nPublic keys: \nAlice: ', alice.public_key, '\nBob: ', bob.public_key)

alice_secret = alice.compute_shared_secret(bob.public_key)
bob_secret = bob.compute_shared_secret(alice.public_key)

print('\nShared secrets: \nAlice: ', alice_secret, '\nBob: ', bob_secret)

alice_key = alice.compute_shared_key(alice_secret)
bob_key = bob.compute_shared_key(bob_secret)

print('\nShared keys: \nAlice: ', alice_key, '\nBob: ', bob_key)

assert alice_key == bob_key, "Keys do not match."

# alice sends encrypted message to Bob
message = "A secret message from Alice to Bob"
encrypted_message = alice.encrypt_message(message, alice_key)
print('\nEncrypted message sent by Alice: ', encrypted_message)

# bob decrypts Alice's message
decrypted_message = bob.decrypt_message(encrypted_message, bob_key)
print('\nDecrypted message read by Bob: ', decrypted_message)

# check that the decrypted message is the same as the original message
assert decrypted_message == message, "Decrypted messages don't match"
