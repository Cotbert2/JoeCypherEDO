import lorenz
from Crypto.Util.number import getPrime, inverse
from utils import Utils

class JoeCypher:
    def __init__(self, x: int, p: int, g: int, show_plot=False):
        if not (1 < x < p - 1):
            raise ValueError(f"The private key x should be 1 < x < p - 1. Recived: x={x}, p={p}")
        self.p = p
        self.g = g
        self.x = x
        self.y = (self.g**self.x) % self.p
        self.myLorenz = lorenz.Lorenz(self.x)
        self.myLorenz.solve_lorenz()
        if show_plot:
            self.myLorenz.draw_attractor()


    def cypher(self, M):
        k = 10
        a = (self.g**k) % self.p
        b = ((self.y**k) * M )% self.p
        a += self.myLorenz.get_position("y", Utils.extractDigits(b))
        b += self.myLorenz.get_position("x", Utils.extractDigits(a))
        self.cipher_text = (a, b)
        return self.cipher_text

    def decypher(self, cypher_message):
        a__1, b__1 = cypher_message
        a_1 = a__1
        b_1 = b__1
        a_1 =int(a__1 - self.myLorenz.get_position("y", Utils.extractDigits(b__1)))
        b_1= int(b__1 -self.myLorenz.get_position("x", Utils.extractDigits(a__1)))
        s = int((a_1**self.x) % self.p)
        s_1 = pow(s, -1, self.p)
        plain_text = (b_1 * s_1) % self.p
        return plain_text

    def getCypherMessage(self):
        return self.cipher_text
