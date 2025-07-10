import cypher2
from Crypto.Util.number import getPrime, inverse


original_text = 56

p = 99999999991
g = 3
x = 30
myJoeCypher = cypher2.JoeCypher(p=p, g= g, x = x)

print("Original text: ", original_text)
cypher_message = myJoeCypher.cypher(original_text)
print("Cypher message: ", cypher_message)
decypher_message = myJoeCypher.decypher(cypher_message)
print("Decypher message: ", decypher_message)