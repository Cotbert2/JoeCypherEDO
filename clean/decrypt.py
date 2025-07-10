import Joe
import utils

p, g, x = 99999999991, 3, 2

myJoeCypher = Joe.JoeCypher(p=p, g=g, x=x)

with open("test.txt", "r", encoding="ascii") as f:
    encoded_string = f.read().replace("\n", "")

decoded_encrypted = utils.Utils.decode_encrypted_floats(encoded_string)
print("Cyphertext read from 'test.txt':")

decrypted_text = ''
for pair in decoded_encrypted:
    val = myJoeCypher.decypher(pair)
    if not (0 <= val < 0x110000):
        print(f"Value out of range: {val}")
        continue
    decrypted_text += chr(val)

print("\nTexto desencriptado:")
print(decrypted_text)