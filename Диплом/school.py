# ____import ____#
import os.path
import jsonpickle


# jsonpickle.set_decoder_options('json', indent=4, ensure_ascii=False)
# jsonpickle.set_encoder_options('json', indent=4, ensure_ascii=False)

# jsonpickle.set_encoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)
# jsonpickle.set_decoder_options('json', indent=4, separators=(',', ': '), ensure_ascii=False)
# ____CLASSES_____#

class Main:
    def __init__(self):
        self.path_file = 'file_name.json'
        self.file_manager = FileManager()

    def load(self):

        shcool = self.file_manager.file_read_json(self.path_file)
        if not shcool is None:
            self.shcool = shcool
        else:
            self.shcool = Shcool(Shcool_Info(), [])

    def start(self):
        """Точка входа в меню программы"""

        x = '-    ШКОЛА     -'
        print('------  ', x, '  ---------')
        print('------------------------------------')
        print('-        ИФОРМАЦИЯ О ШКОЛЕ         -')
        print('-           нажмите "1"            -')
        print('-      ИНФОРМАЦИЯ ОБ УЧЕНИКАХ      -')
        print('-           нажмите "2"            -')
        print('------------------------------------')
        menu_num = int(input())
        if menu_num == 1:
            Shcool_Info_Chang()
        elif menu_num == 2:
            Students_List.add_student()
            """  Пусть будет пока   """





    def menu_shcool(self):

        x = '-    ШКОЛА     -'
        print('------  ', x, '  ---------')
        print('------------------------------------')
        print('-          НОМЕР ШКОЛЫ             -')
        print('-           нажмите "1"            -')
        print('-         АДРЕСС ШКОЛЫ             -')
        print('-           нажмите "2"            -')
        print('------------------------------------')
        menu_num = input()

    def menu_students(self):
        """Внесение изменений в список студентов"""

        x = '-    ШКОЛА     -'
        print('------  ', x, '  ---------')
        print('------------------------------------')
        print('-   ПРОСМОТРЕТЬ СПИСОК УЧЕНИКОВ    -')
        print('-           нажмите "1"            -')
        print('-        ДОБАВИТЬ УЧЕНИКА          -')
        print('-           нажмите "2"            -')
        print('-        УДАЛИТЬ УЧЕНИКА           -')
        print('-           нажмите "3"            -')
        print('------------------------------------')

        """  проаверка ввода меню    """
        menu_num = input()
        if menu_num == 1:
            Students_List.add_student()
        elif menu_num ==2:
            Students_List.add_student()

    def save(self):
        self.file_manager.file_write_json(self.path_file, self.shcool)


class Shcool:
    def __init__(self, shcool_info,adress ,students):
        self.shcool_info = shcool_info
        self.students = students

    def get_list(self):
        return self.students

    def get_info(self):
        return self.shcool_info


class Shcool_Info:
    """Информация о школе"""

    def __init__(self, name_shcool='no name', adress_shcool='no name', count_students=0):
        self.name_shcool = name_shcool
        self.adress_shcool = adress_shcool
        self.count_students = count_students


class Shcool_Info_Chang:
    """Меню измения инфы о школе"""

    def __init__(self, shcool_info):
        self.shcool_info = shcool_info


class Student:
    """анкетные данные ученика"""

    def __init__(self, student_id, first_name_student, last_name_student, age_student,
                 number_class):
        self.student_id = student_id
        self.first_name_student = first_name_student
        self.last_name_student = last_name_student
        self.age_student = age_student
        self.number_class = number_class


class Students_List:
    """обработка списка учеников"""

    def __init__(self, students):
        self.students = students

    def add_student(self):
        """Добавление в список"""
        pass

    def del_student(self):
        pass


class FileManager:

    def __init__(self):
        pass

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


# class Check_Input:
#     def __init__(self, data_format, data_entry):
#         name_str = 1
#         symb_str = 2
#         data_str = 3
#
#         self.data_format = data_format
#         self.data_entry = data_entry
#         data_entry_f = data_entry[:1]
#         if data_format == name_str:
#             if not data_entry.isalpha():
#                 data_entry = input('Правильно вводите имена и фамилии:')
#             elif not data_entry_f.isupper():
#                 print(data_entry_f)
#                 data_entry = input('Правильно вводите символы:')


# ___FUNCTIONS_____#

def check_input_data(data_entry):
    data_entry_f = data_entry[:1]
    print(data_entry_f)
    if data_entry.isalpha():
        data_entry = input('Правильно вводите имена и фамилии:')
    elif not data_entry_f.isupper():
        print(data_entry_f)
        data_entry = input('Правильно вводите символы:')


def check_input_str(str_entry):
    str_entry_f = str_entry.isalpha([1])
    if not str_entry.isalpha():
        str_entry = input('Правильно вводите имена и фамилии:')
    elif not str_entry_f.isupper():
        print(str_entry_f)
        str_entry = input('Правильно вводите символы:')


def int_input(str_entry):
    digit = input()
    while not is_valid(digit):
        digit = input()
    else:
        digit = int(digit)
    return digit


def is_valid(int_input):
    if int_input.isdigit():
        n = int(int_input)
        return True
    print('Пожалуйста, введите число!')
    return False


# ___GENERAL CODE______#
if __name__ == '__main__':
    main = Main()
    main.load()
    main.start()
    main.save()
    main.menu_main()
# lname = input('Введите Фамилию ученика:')
# a_student = input('Введите возраст ученика:')
# n_class = input('Введите класс ученика:')
# student = Student(fname, lname, a_student, n_class)
# print(student.first_name_student)
