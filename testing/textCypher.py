
import cypher2

#Define the original text to encrypt
# plaint_text_to_encrypt = """
# Linus Torvals is a Rockstar, he is the creator of Linux and Git.
# """

plaint_text_to_encrypt = """L"""


cypherMessage = []
originalMessage = []

myJoeCypher = cypher2.JoeCypher()

for char in plaint_text_to_encrypt:
    # Convert character to ASCII value
    # Encrypt the ASCII value
    originalMessage.append(ord(char))
    cypherMessage.append(myJoeCypher.cypher(ord(char)))

print("Original message: ", originalMessage)
print("Cypher message: ", cypherMessage)


# Encrypt the text
cypher_text = myJoeCypher.cypher(5200)
print("Cipher text: ", cypher_text)

# Decrypt the text
decypher_text = myJoeCypher.decypher(myJoeCypher.x, cypher_text)
print("Decypher text: ", decypher_text)

# Check if the decrypted text matches the original text
