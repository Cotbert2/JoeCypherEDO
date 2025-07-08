import cypher2

original_text = 56


myJoeCypher = cypher2.JoeCypher(p=467, g= 2, x = 36)

print("Original text: ", original_text)
cypher_message = myJoeCypher.cypher(original_text)
print("Cypher message: ", cypher_message)
decypher_message = myJoeCypher.decypher(cypher_message)
print("Decypher message: ", decypher_message)