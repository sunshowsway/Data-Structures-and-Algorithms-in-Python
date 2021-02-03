class CaesarCipher:
    def __init__(self, shift):
        self._forward = "".join(chr((k+shift) % 26 + ord("A")) for k in range(26))
        self._backward = "".join(chr((k-shift) % 26 + ord("A")) for k in range(26))

    def encrypt(self, message):
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")
                msg[k] = code[j]
        return "".join(msg)