from Crypto.Util.number import getPrime
import struct
import base64

class Utils:
    def extractDigits(number):
        number = abs(int(number))
        if number < 10:
            return number * 11
        elif number >= 100:
            return int(str(number)[:2])
        return number


    def encode_encrypted_floats(encrypted_list):
        raw_bytes = b''
        for a, b in encrypted_list:
            raw_bytes += struct.pack('>d', a)
            raw_bytes += struct.pack('>d', b)
        return base64.b85encode(raw_bytes).decode('ascii')


    def decode_encrypted_floats(encoded_string):
        raw_bytes = base64.b85decode(encoded_string.encode('ascii'))
        floats = []
        for i in range(0, len(raw_bytes), 16):
            a = struct.unpack('>d', raw_bytes[i:i + 8])[0]
            b = struct.unpack('>d', raw_bytes[i + 8:i + 16])[0]
            floats.append((a, b))
        return floats

