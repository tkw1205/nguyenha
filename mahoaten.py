def mahoaten(plaintext, a):
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            offset = ord('A')
            mh = chr((ord(i.upper()) - offset + a) % 26 + offset)
            ciphertext += mh
        else:
            ciphertext += i
    return ciphertext

# Tên: Hà, STT: 13
plaintext = "HA"
k = 13
ciphertext = mahoaten(plaintext, k)
print("Tên sau khi được mã hóa:", ciphertext)