def rsa_encrypt(message, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if e >= phi or gcd(e, phi) != 1:
        raise ValueError("e không hợp lệ")

    encrypted = []
    for char in message:
        m = ord(char) 
        c = pow(m, e, n)
        encrypted.append(c)

    return encrypted

p = 17
q = 23
e = 5
message = "NGUYENTHITHUHA"

cipher_text = rsa_encrypt(message, p, q, e)

print("Cipher:", cipher_text)
