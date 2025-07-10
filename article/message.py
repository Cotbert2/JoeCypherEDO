import cypher2
from Crypto.Util.number import getPrime
import struct
import base64
import math
from collections import Counter


def encode_encrypted_floats(encrypted_list):
    raw_bytes = b''
    for a, b in encrypted_list:
        raw_bytes += struct.pack('>d', a)
        raw_bytes += struct.pack('>d', b)
    return base64.b85encode(raw_bytes).decode('ascii')

def decode_encrypted_floats(encoded_string):
    raw_bytes = base64.b85decode(encoded_string.encode('ascii'))
    floats = []
    for i in range(0, len(raw_bytes), 16):
        a = struct.unpack('>d', raw_bytes[i:i+8])[0]
        b = struct.unpack('>d', raw_bytes[i+8:i+16])[0]
        floats.append((a, b))
    return floats


def shannon_entropy(s):
    if not s:
        return 0.0
    length = len(s)
    freq = Counter(s)
    probs = [count / length for count in freq.values()]
    entropy = -sum(p * math.log2(p) for p in probs)
    return entropy

def compare_entropy(str1, str2):
    entropy1 = shannon_entropy(str1)
    entropy2 = shannon_entropy(str2)

    print(f"Entropía de str1: {entropy1:.4f}")
    print(f"Entropía de str2: {entropy2:.4f}")

    if entropy1 > entropy2:
        print("str1 tiene mayor entropía.")
    elif entropy1 < entropy2:
        print("str2 tiene mayor entropía.")
    else:
        print("Ambas cadenas tienen la misma entropía.")


p = getPrime(32)
g = 3
x = 2
myJoeCypher = cypher2.JoeCypher(p=p, g=g, x=x)

original_text = "This is a test message to demonstrate the JoeCypher encryption and decryption process."


encrypted_list = [myJoeCypher.cypher(ord(char)) for char in original_text]

encoded_string = encode_encrypted_floats(encrypted_list)




print("Encrypted string:")
print(encoded_string)

decoded_encrypted = decode_encrypted_floats(encoded_string)
print("🔐 Decoded Text")
print(decoded_encrypted)

compare_entropy(original_text, encoded_string)
decrypted_text = ''.join(chr(myJoeCypher.decypher(pair)) for pair in decoded_encrypted)

print("\nDecrypted text:")
print(decrypted_text)
