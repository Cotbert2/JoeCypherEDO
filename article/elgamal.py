from Crypto.Util.number import getPrime, inverse
from random import randint

# 1. Generar claves ElGamal
def generar_claves():
    p = getPrime(256)
    g = randint(2, p - 2)
    x = randint(1, p - 2)       # Clave privada
    y = pow(g, x, p)            # Clave pública
    return p, g, x, y

# 2. Cifrar un carácter (como número)
def cifrar(m, p, g, y):
    k = randint(1, p - 2)
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    return a, b

# 3. Descifrar
def descifrar(a, b, p, x):
    s = pow(a, x, p)
    s_inv = inverse(s, p)
    m = (b * s_inv) % p
    return m

# 4. Convertir texto a lista de números
def texto_a_numeros(texto):
    return [ord(c) for c in texto]

# 5. Convertir lista de números a texto
def numeros_a_texto(numeros):
    return ''.join(chr(n) for n in numeros)

# --------- DEMO ---------
# Mensaje a cifrar
mensaje = "Hola"

# Generar claves
p, g, x, y = generar_claves()

# Convertir texto a números
numeros = texto_a_numeros(mensaje)

# Cifrar cada carácter
cifrado = [cifrar(m, p, g, y) for m in numeros]

# Mostrar el texto cifrado (pares (a, b))
print("🔐 Texto cifrado (ElGamal):")
for i, (a, b) in enumerate(cifrado):
    print(f"Letra '{mensaje[i]}' → Cifrado: (a={a}, b={b})")

# Descifrar para comprobar
descifrado = [descifrar(a, b, p, x) for (a, b) in cifrado]
texto_recuperado = numeros_a_texto(descifrado)

print("\n🔓 Texto descifrado:", texto_recuperado)
