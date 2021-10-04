s = input("Cимволы: ")
sym = ''
for i in range(len(s)):
    code = ord(s[i])
    if code >= 48 and code <= 57:
        sym += s[i]
print(sym)