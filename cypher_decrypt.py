import random
from Crypto.Util.number import getPrime, inverse

def generate_keys():
    # Generate a large prime number
    p = getPrime(1024)

    # Choose a random number as the private key
    private_key = random.randint(2, p - 2)

    # Calculate the public key
    public_key = pow(g, private_key, p)

    return public_key, private_key

def encrypt(public_key, message):
    # Generate a random number as the ephemeral key
    k = random.randint(2, p - 2)

    # Calculate the ciphertext
    c1 = pow(g, k, p)
    c2 = (message * pow(public_key, k, p)) % p

    return c1, c2

def decrypt(private_key, ciphertext):
    c1, c2 = ciphertext

    # Calculate the shared secret
    shared_secret = pow(c1, private_key, p)

    # Calculate the plaintext
    plaintext = (c2 * inverse(shared_secret, p)) % p

    return plaintext

# Example usage
g = 2  # Generator
p = 123456789  # Prime modulus

# Generate keys
public_key, private_key = generate_keys()

# Encrypt a message
message = 42
ciphertext = encrypt(public_key, message)

# Decrypt the ciphertext
plaintext = decrypt(private_key, ciphertext)

print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", plaintext)