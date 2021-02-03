class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 256
        decoder = [None] * 256
        for k in range(256):
            encoder[k] = chr((k+shift) % 256 + ord("Ѐ"))
            decoder[k] = chr((k-shift) % 256 + ord("Ѐ"))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("Ѐ")
                msg[k] = code[j]
        return "".join(msg)