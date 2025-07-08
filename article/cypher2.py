import lorenz
from Crypto.Util.number import getPrime, inverse
import extractDigits

class JoeCypher:
    def __init__(self, x: int, p: int, g: int):
        if not (1 < x < p - 1):
            raise ValueError(f"La clave privada x debe cumplir 1 < x < p - 1. Recibido: x={x}, p={p}")

        self.p = p
        self.g = g
        self.x = x
        self.y = (self.g**self.x) % self.p


    def cypher(self, M):

        #Encriptacion
        k = 10
        a = (self.g**k) % self.p
        b = ((self.y**k) * M )% self.p


        self.myLorenz = lorenz.Lorenz(self.x)
        self.myLorenz.solve_lorenz()
        # print(f"b: {b}")

        a += self.myLorenz.getPosition("y", extractDigits.extractDigits(b))
        b += self.myLorenz.getPosition("x", extractDigits.extractDigits(a))

        #print posiciones
        print("posiciones")
        print(self.myLorenz.getPosition("x", extractDigits.extractDigits(a)))
        print(self.myLorenz.getPosition("y", extractDigits.extractDigits(b)))


        self.cipher_text = (a, b)
        print("Cipher text: ", self.cipher_text)
        return self.cipher_text

    def decypher(self, cypher_message):
        print("mensaje recibido: ", cypher_message)
        #Desencriptacion
        self.myLorenz = lorenz.Lorenz(self.x)
        self.myLorenz.solve_lorenz()


        a__1, b__1 = cypher_message
        a_1 = a__1
        b_1 = b__1
        a_1 =int(a__1 - self.myLorenz.getPosition("y", extractDigits.extractDigits(b__1)))
        b_1= int(b__1 -self.myLorenz.getPosition("x", extractDigits.extractDigits(a__1)))
        #impirimir posiciones
        print("posiciones")
        print(self.myLorenz.getPosition("x", extractDigits.extractDigits(a__1)))
        print(self.myLorenz.getPosition("y", extractDigits.extractDigits(b__1)))

        # print(f"a_1: {a_1}")
        # print(f"b_1: {b_1}")

        # print("p: ", self.p)
        # print("x: ", self.x)
        s = int((a_1**self.x) % self.p)
        # print(f"s: {s}")
        s_1 = pow(s, -1, self.p)
        # print(f"s_1: {s_1}")
        plain_text = (b_1 * s_1) % self.p
        # print("Plain text: ", plain_text)
        return plain_text

    #getter for cypher message
    def getCypherMessage(self):
        return self.cipher_text
