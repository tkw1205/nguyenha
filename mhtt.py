def mahoa(text, k=13):
    kq = []
    for ch in text:
        if 'A' <= ch <= 'Z':  
            code = ord(ch) - ord('A')
            new_code = (code + k) % 26
            kq.append(chr(new_code + ord('A')))
        elif 'a' <= ch <= 'z':  
            code = ord(ch) - ord('a')
            new_code = (code + k) % 26
            kq.append(chr(new_code + ord('a')))
        else:
            kq.append(ch)
    return ''.join(kq)

ten = "HA"
k = 13

kqmahoa = mahoa(ten, k)

print("Kết quả sau khi mã hóa:", kqmahoa)
