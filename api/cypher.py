import lorenz

import extractDigits
p = 99991
g = 6
# Clave privada para A
x = 35
y = (g**x) % p


public_key = (p, g, y)
print("Public key: ", public_key)

#Encriptacion
M = 200
k = 10
a = (g**k) % p
b = ((y**k) * M )% p


myLorenz = lorenz.Lorenz(3)
myLorenz.solve_lorenz()
print(f"b: {b}")

a += myLorenz.getPosition("y", extractDigits.extractDigits(b))
b += myLorenz.getPosition("x", extractDigits.extractDigits(a))


cipher_text = (a, b)
print("Cipher text: ", cipher_text)

class Cypher ():
    def __init__(self, p, g, y, M, k, beta):
        self.p = p
        self.g = g
        self.y = y
        self.M = M
        self.k = k
        self.beta = beta
        self.lorenz = lorenz.Lorenz(self.beta)

    def encrypt(self):
        a = (self.g**self.k) % self.p
        b = ((self.y**self.k) * self.M )% self.p
        a += self.lorenz.getPosition("y", extractDigits.extractDigits(b))
        b += self.lorenz.getPosition("x", extractDigits.extractDigits(a))
        return (a, b)

    def decrypt(self, cipher_text, x):
        a__1, b__1 = cipher_text
        a_1 =int(a__1 - self.lorenz.getPosition("y", extractDigits.extractDigits(b__1)))
        b_1= int(b__1 -self.lorenz.getPosition("x", extractDigits.extractDigits(a__1)))
        s = int((a_1**x) % self.p)
        s_1 = pow(s, -1, self.p)
        plain_text = (b_1 * s_1) % self.p
        return plain_text

#Desencriptacion


a__1, b__1 = cipher_text
a_1 =int(a__1 - myLorenz.getPosition("y", extractDigits.extractDigits(b__1)))
b_1= int(b__1 -myLorenz.getPosition("x", extractDigits.extractDigits(a__1)))

print(f"a_1: {a_1}")
print(f"b_1: {b_1}")

s = int((a_1**x) % p)
print(f"s: {s}")
s_1 = pow(s, -1, p)
print(f"s_1: {s_1}")
plain_text = (b_1 * s_1) % p
print("Plain text: ", plain_text)