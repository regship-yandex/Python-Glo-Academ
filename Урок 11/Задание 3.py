ip = "192.168.255.000"
flag = True
i = 0
ip_sp = ip.split(".")
while i < len(ip_sp):
    ip_data = int(ip_sp[i])
    if ip_data < 0 or ip_data > 255:
        flag = False
        break
    i += 1
if flag == True:
    print('Yes')
else:
    print('NO')