import cypher2

myJoeCypher = cypher2.JoeCypher()


original_text = """
This is a test message to demonstrate the JoeCypher encryption and decryption process.
"""


encrypted_text = []


for i in range(len(original_text)):
    #print char value
    encrypted_text.append(
    myJoeCypher.cypher(ord(original_text[i])))


print("Original text: ", original_text)
print("Encrypted text: ", encrypted_text)


decyphered_text = ""

for i in range(len(encrypted_text)):
    #print char value
    decyphered_text += chr(myJoeCypher.decypher(encrypted_text[i]))

print("Encrypted text: ", decyphered_text)