symb1 = input("Первый символ: ")
symb2 = input("Второй символ: ")
if ord(symb1) > ord(symb2):
    symb1, symb2 = symb2, symb1
s1 = ord(symb1)
s2 = ord(symb2)
symb = ''
for i in range(s1, s2+1):
    s = chr(i)
    symb += s + " "
print(symb)