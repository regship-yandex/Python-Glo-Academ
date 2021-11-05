import os.path
import jsonpickle

class Shcool_data:

    def __init__(self):
        self.students = []
        self.name_shcool = "Нет информации"
        self.adress_shcool = "Нет информации"

    def get_list(self):
        return self.students

    def get_count_students(self):
        return len(self.students)


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

    def load(self):
        shcool = self.file_manager.file_read_json(self.path_file)
        if not shcool is None:
            self.shcool = shcool
        else:
            self.shcool = Shcool_data()

    def start(self):
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
            elif menu_num == "99":
                self.add_student()
                self.save()
            elif menu_num == "9":
                self.show_info()
            elif menu_num == "0":
                break
            print('Выберите нужный пункт меню')


    def menu_shcool(self):
        while True:
            print('------         ШКОЛА        --------')
            print('------------------------------------')
            print('-          НОМЕР ШКОЛЫ             -')
            print('-           нажмите "1"            -')
            print('-          АДРЕСС ШКОЛЫ            -')
            print('-           нажмите "2"            -')
            print('-=   главное меню нажмите "0"     =-')
            print('------------------------------------')

            """  проверка ввода меню    """
            menu_num = input()
            if menu_num == "1":
                self.add_name_shcool()
            elif menu_num == "2":
                self.add_adress_shcool()
            elif menu_num == "0":
                self.menu_shcool()
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
                self.print_list()
                self.add_student()
            elif menu_num == "3":
                self.del_student()
            elif menu_num == "0":
                break
            print('Выберите нужный пункт меню')

    def add_name_shcool(self):
        self.name_shcool = input('Номер школы: ')
        self.print_info()
        self.menu_shcool()

    def add_adress_shcool(self):
        self.Shcool_data().adress_shcool = input('Адрес школы: ')


    def save(self):
        """Сохраняет данные в файл"""
        self.file_manager.file_write_json(self.path_file, self.shcool)

    def show_info(self):
        print(f'имя={self.shcool.name_shcool}  адрес={self.shcool.adress_shcool} '
              f'всего уч= {self.shcool.get_count_students()}')

        for i in range(len(self.shcool.students)):
            print(i+1,
                  self.shcool.students[i].first_name_student,
                  self.shcool.students[i].last_name_student
                  )

    def add_student(self):
        sh = self.shcool
        first_name_student = input("введите имя ученика: ")
        last_name_student = input("введите фамилию ученика: ")
        age_student = input("введите возраст ученика: ")   # на дурака
        number_class = input("введите класс ученика: ")  # на дурака
        student = Student(first_name_student, last_name_student, age_student, number_class)
        sh.students.append(student)
        print(sh.get_count_students())

        for i in range(len(sh.students)):
            print(i+1, sh.students[i].first_name_student, sh.students[i].last_name_student,
                  sh.students[i].ag_student, sh.students[i].number_class)

        sh.students.remove(sh.students[2]) # так удаляем

        print(sh.get_count_students())

        for i in range(len(sh.students)):
            print(i, sh.students[i].student_id, sh.students[i].first_name_student)


        print(sh.get_count_students())

        for i in range(len(sh.students)):
            print(i, sh.students[i].student_id, sh.students[i].first_name_student)
        print(len(sh.students))

    def del_student(self):

        self.print_list()
        id_stud = int_input('Выберите номер студента: ')

        ind = id_stud-1
        self.students.remove(self.students[ind])
    def print_list(self):
        for i in range(len(self.students)):
            print(i+1, self.students[i].student_id, self.students[i].first_name_student)


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
        # with open(file_name, "w") as write_file:
        #     json.dump(obj, write_file)
        file = open(file_name, 'w', encoding='utf8')
        text = jsonpickle.encode(obj)
        file.write(text)
        file.close()

    def file_read_json(self, file_name):
        if not os.path.exists(file_name):
            return None

        # with open(file_name, "r") as read_file:
        #     obj = json.load(read_file)

        file = open(file_name, 'r', encoding='utf8')
        text = file.read()
        file.close()
        obj = jsonpickle.decode(text)
        return obj



if __name__ == '__main__':
    main = Shcool_Manager()
    main.load()
    main.start()
    main.save()

