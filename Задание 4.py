s = input()
symb = ord(s)
if symb >= 65  and symb <= 90:
    print(s.lower())
elif symb >= 97  and symb <= 122:
    print(s.upper())
else:
    print(s)