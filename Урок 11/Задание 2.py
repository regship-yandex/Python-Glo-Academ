path = "D:\MyDocuments\Python\Courses\план обучения.txt"

i = 0
path_sp = path.split("\\")
while i < len(path_sp):
    print(path_sp[i])
    i += 1