from User import User
from File_manager import FileManager

class UserResultStorage:

    def __init__(self, name_file = "my_test.csv"):
        self.user_list = []
        self.name_file = name_file
        self.fm = FileManager()
        self.load()

    def load(self):
        file_text = self.fm.file_read(self.name_file).strip('\n')
        data = file_text.split('\n')
        for line in data:
            # print(line)
            user = User("l")
            user.load(line)
            self.user_list.append(user)
            # print(user.result_test())

    def save(self):
        file_text = ""
        for user in self.user_list:
            # print(user.result_test())
            file_text = file_text + user.to_text()
        self.fm.file_write(self.name_file, file_text)

    def add_user(self, user):
        file_text = user.to_text()
        self.fm.file_add(self.name_file, file_text)

    def show_user_result(self):
        self.load()
        name = 'Имя'
        count = 'Правильных ответов'
        result = 'Результат'
        print(f'{name:6}{count:9} {result:1}')

        for i in  range(len(self.user_list)):
            print(
                f'{self.user_list[i].name:6}{self.user_list[i].count_right_answer:30} '
                f'{self.user_list[i].result:1}')
