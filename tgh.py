#ElGamal public key generation

p = 99991
g = 6
# Clave Privada para A
x = 35
y = (g**x) % p


public_key = (p, g, y)
print("Public key: ", public_key)

#Encriptacion
M = 20
k = 10
a = (g**k) % p
b = ((y**k) * M )% p

print(f"b: {b}")
cipher_text = (a, b)
print("Cipher text: ", cipher_text)

#Desencriptacion
a_1, b_1 = cipher_text
s = (a_1**x) % p
print(f"s: {s}")
s_1 = pow(s, -1, p)
print(f"s_1: {s_1}")
plain_text = (b_1 * s_1) % p
print("Plain text: ", plain_text)