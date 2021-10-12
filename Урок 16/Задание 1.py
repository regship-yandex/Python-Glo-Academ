def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)

    return field


def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()


def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True
    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True
    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
        return True

    return False


def end_game(field):
    if win(field):
        return True
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
    return True

def int_input(str):
    print(str)
    digit = input()
    while not is_valid(digit):
        digit = input()
    else:
        digit = int(digit)
    return digit

def field_false(field, row, column):
    if field[row - 1][column - 1] != '*':
        return True
    else:
        return False

def is_valid(int_input):
    if int_input.isdigit():
        n = int(int_input)
        if 1<=n and n<=3:
            return True
    return False


#       Основной код         #

while True:
    field = create_field()
    curent_symbol = 'x'

    while not end_game(field):
        print_field(field)
        print('Введите координаты для', curent_symbol)
        row = int_input('номер строки')
        column = int_input('номер столбца')
        # if field_false(field, row, column):
        if field[row - 1][column - 1] != '*':
            print('!   Поле занято   !')
            continue
        field[row - 1][column - 1] = curent_symbol

        if curent_symbol == 'x':
            curent_symbol = 'o'
        else:
            curent_symbol = 'x'

    if curent_symbol == 'x':
        print('Ура! Вы победил О.')
    else:
        print('Ура! Вы победил Х.')
    output = input('Хотите еще сыграть? (да, нет)')
    if output in 'lfLfLFДаДАда':
        True
    else:
        print('Мы прощаемся с вами')
        False
