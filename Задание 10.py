line = input()
line_len = len(line)
count_line = 1
for i in range(line_len):
    code = ord(line[i])
    if code == 32:
        count_line += 1
if count_line <= 1:
    count_line = 0
print(count_line)