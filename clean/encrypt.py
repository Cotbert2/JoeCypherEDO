import Joe
import utils

p = 99999999991
g = 3
x = 2
myJoeCypher = Joe.JoeCypher(p=p, g=g, x=x)

with open("test.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

encrypted_list = [myJoeCypher.cypher(ord(char)) for char in original_text]
encoded_string = utils.Utils.encode_encrypted_floats(encrypted_list)

with open("test.txt", "w", encoding="ascii") as f:
    f.write(encoded_string)

print("Encrypted text saved to 'test.txt'")
print(encoded_string)