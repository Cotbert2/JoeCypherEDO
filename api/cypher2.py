import lorenz
import extractDigits

class JoeCypher:
    def __init__(self, M):
        self.M = M
        self.p = 99991
        g = 6
        # Clave privada para A
        x = 35
        y = (g**x) % self.p


        public_key = (self.p, g, y)
        print("Public key: ", public_key)

        #Encriptacion
        M = 3000
        k = 10
        a = (g**k) % self.p
        b = ((y**k) * M )% self.p


        self.myLorenz = lorenz.Lorenz(x)
        self.myLorenz.solve_lorenz()
        print(f"b: {b}")

        a += self.myLorenz.getPosition("y", extractDigits.extractDigits(b))
        b += self.myLorenz.getPosition("x", extractDigits.extractDigits(a))


        self.cipher_text = (a, b)
        print("Cipher text: ", self.cipher_text)

    def decypher(self, x, cypher_message):
        #Desencriptacion
        a__1, b__1 = cypher_message
        a_1 =int(a__1 - self.myLorenz.getPosition("y", extractDigits.extractDigits(b__1)))
        b_1= int(b__1 -self.myLorenz.getPosition("x", extractDigits.extractDigits(a__1)))

        print(f"a_1: {a_1}")
        print(f"b_1: {b_1}")

        print("p: ", self.p)
        print("x: ", x)
        s = int((a_1**x) % self.p)
        print(f"s: {s}")
        s_1 = pow(s, -1, self.p)
        print(f"s_1: {s_1}")
        plain_text = (b_1 * s_1) % self.p
        print("Plain text: ", plain_text)
        return plain_text

    #getter for cypher message
    def getCypherMessage(self):
        return self.cipher_text
