import os.path
import jsonpickle


class Shcool:

    def __init__(self, name, adress, student=None):
        if student is None:
            student = []
        self.students = student
        self.name_shcool = name
        self.adress_shcool = adress


#
#     def get_list(self):
#         return self.students
#
#     def get_count_students(self):
#         return len(self.students)

class Student:
    """анкетные данные ученика"""

    def __init__(self, first_name_student, last_name_student, age_student,
                 number_class):
        self.first_name_student = first_name_student
        self.last_name_student = last_name_student
        self.age_student = age_student
        self.number_class = number_class


class Shcool_Manager:

    def __init__(self):
        self.path_file = 'file_name.json'
        self.file_manager = FileManager()
        self.students = []
        self.name_shcool = "Нет информации"
        self.adress_shcool = "Нет информации"

    def get_list(self):
        return self.students

    def get_count_students(self):
        return len(self.students)

    def load(self):
        self.shcool = self.file_manager.file_read_json(self.path_file)
        if not self.shcool is None:
            self.name_shcool = self.shcool.name_shcool
            self.adress_shcool = self.shcool.adress_shcool
            self.students = self.shcool.students

    def menu_start(self):
        """Точка входа в меню программы"""
        while True:
            print('-------    Главное меню    ---------')
            print('------------------------------------')
            print('-        ИФОРМАЦИЯ О ШКОЛЕ         -')
            print('-           нажмите "1"            -')
            print('-      ИНФОРМАЦИЯ ОБ УЧЕНИКАХ      -')
            print('-           нажмите "2"            -')
            print('-   --   ВЫЙТИ ИЗ ПРОГРАММЫ   --   -')
            print('-           нажмите "0"            -')
            print('------------------------------------')
            menu_num = input()
            if menu_num == "1":
                self.menu_shcool()
            elif menu_num == "2":
                self.menu_students()
            # elif menu_num == "99":
            #     self.add_student()
            #     self.save()
            # elif menu_num == "9":
            #     self.show_info()
            elif menu_num == "0":
                break
            print('Выберите нужный пункт меню')

    def menu_shcool(self):
        while True:
            self.show_info()
            print('---------      ШКОЛA     -----------')
            print('------------------------------------')
            print('-          НОМЕР ШКОЛЫ             -')
            print('-           нажмите "1"            -')
            # print('-          АДРЕСС ШКОЛЫ            -')
            # print('-           нажмите "2"            -')
            print('-=   главное меню нажмите "0"     =-')
            print('------------------------------------')

            """  проверка ввода меню    """
            menu_num = input()
            if menu_num == "1":
                self.add_name_shcool()
                self.save()
            elif menu_num == "0":
                # self.start()
                break
            print('Выберите нужный пункт меню')

    def menu_students(self):
        """Внесение изменений в список студентов"""
        while True:
            print('---------     УЧЕНИКИ    -----------')
            print('------------------------------------')
            print('-   ПРОСМОТРЕТЬ СПИСОК УЧЕНИКОВ    -')
            print('-           нажмите "1"            -')
            print('-        ДОБАВИТЬ УЧЕНИКА          -')
            print('-           нажмите "2"            -')
            print('-        УДАЛИТЬ УЧЕНИКА           -')
            print('-           нажмите "3"            -')
            print('-=    главное меню нажмите "0"    =-')
            print('------------------------------------')

            """  проверка ввода меню    """
            menu_num = input()
            if menu_num == "1":
                self.print_list()
            elif menu_num == "2":
                # self.print_list()
                self.add_student()
                self.save()
            elif menu_num == "3":
                self.print_list()
                self.del_student()
                self.save()
            elif menu_num == "0":
                break
            print('Выберите нужный пункт меню')

    def add_name_shcool(self):
        self.name_shcool = valid_digit('Номер школы: ', 1, 5000)
        # self.save()
        self.adress_shcool = input('Адрес школы: ')
        # self.save()
        # self.menu_shcool()

    def save(self):
        """Сохраняет данные в файл"""
        shcool_inf = Shcool(self.name_shcool, self.adress_shcool, self.students)
        self.file_manager.file_write_json(self.path_file, shcool_inf)

    def show_info(self):

        print(f'Школа = {self.name_shcool}  адрес = {self.adress_shcool} \n'
              f'всего учеников = {self.get_count_students()}')

    def add_student(self):
        sh = self.shcool
        first_name_student = valid_symbol("введите имя ученика: ")
        last_name_student = valid_symbol("введите фамилию ученика: ")
        age_student = valid_digit("введите возраст ученика: ", 6, 19)  # на дурака
        number_class = valid_digit("введите класс ученика: ", 1, 11)  # на дурака
        student = Student(first_name_student, last_name_student, age_student, number_class)
        sh.students.append(student)

        # print(sh.get_count_students())
        # print(len(sh.students))

        # for i in range(len(sh.students)):
        #     print(i+1, sh.students[i].first_name_student, sh.students[i].last_name_student,
        #           sh.students[i].age_student, sh.students[i].number_class)
        #
        # # sh.students.remove(sh.students[2])  # так удаляем
        # print(len(sh.students))
        #
        # for i in range(len(sh.students)):
        #     print(i, sh.students[i].student_id, sh.students[i].first_name_student)

    def del_student(self):
        # self.print_list()
        id_stud = valid_digit('Выберите номер ученика: ', 1, len(self.students) + 1)
        ind = id_stud - 1
        self.students.remove(self.students[ind])

    def print_list(self):
        if not len(self.students) == 0:
            print(('________________________________________'))
            for i in range(len(self.shcool.students)):
                print(
                    f'{i + 1:3} {self.students[i].first_name_student :8} {self.students[i].last_name_student:10}{self.students[i].age_student:5}{self.students[i].number_class:5}')
        else:
            print('Список студенов пуст')
            print(('________________________________________'))


class FileManager:
    def __init__(self):
        pass
        # self.file_nam = file_nam

    def file_write(self, file_name, text):
        file = open(file_name, 'w', encoding='utf8')
        file.write(text)
        file.close()

    def file_read(self, file_name):
        if not os.path.exists(file_name):
            return ""
        file = open(file_name, 'r', encoding='utf8')
        test_result = file.read()
        file.close()
        return test_result

    def file_add(self, file_name, test):
        file = open(file_name, 'a', encoding='utf8')
        file.write(test)
        file.close()

    def file_write_json(self, file_name, obj):
        file = open(file_name, 'w', encoding='utf8')
        text = jsonpickle.encode(obj)
        file.write(text)
        file.close()

    def file_read_json(self, file_name):
        if not os.path.exists(file_name):
            return None

        file = open(file_name, 'r', encoding='utf8')
        text = file.read()
        file.close()
        obj = jsonpickle.decode(text)
        return obj


def valid_digit(str, min_d, max_d):
    digit = ""
    while not f'{digit}'.isdigit():
        digit = input(str)
        while not is_valid(digit):
            digit = input(str)

        digit = int(digit)
        if not (min_d <= digit and digit <= max_d):
            print(f'от {min_d} до {max_d}')
            digit = ""
        else:
            # print("OK",digit)
            return digit
    return digit


def is_valid(int_input):
    if int_input.isdigit():
        # n = int(int_input)
        return True
    print('Пожалуйста, введите число!')
    return False


def valid_symbol(str):
    isff = False
    while not isff:
        isff = True
        vs = input(str)
        if not vs.istitle():
            isff = False
        if not vs.isalpha():

            isff = False

        # if isff == False:
        #     print("Эти бла бла")
        # else:
        #     print("OK", vs)

    # if (ss.istitle()):
    #     print('ss.istitle')
    # if (ss.isdigit()): print('ss.isdigit')
    # if (ss.isupper()): print('ss.isupper')
    # if (ss.isascii()): print('ss.isascii')
    # if (ss.isidentifier()): print('ss.isidentifier')

    # return input(str)
    return vs


if __name__ == '__main__':
    # while True:
    #     #     # valid_digit("тест ", 0, 10)
    #     valid_symbol("str")

    main = Shcool_Manager()
    main.load()
    main.menu_start()
    main.save()
