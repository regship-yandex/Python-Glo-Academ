from File_manager import FileManager


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def to_text(self):
        return (f'{self.text};{self.answer}\n')


class QuestionStorage:
    def __init__(self, name_file="my_Question.json"):
        self.questions = []
        self.name_file = name_file
        self.fm = FileManager()
        self.load()

    def get_quest(self):
        return self.questions

    def get_queastions(self):
        return self.questions

    def add_quest(self, queastion):
        self.questions.append(queastion)
        return self.questions

    def dell_quest(self, question):
        self.questions.remove(question)
        return self.questions

    def dell_quest_by_index(self, index):
        question = self.questions[index]
        self.dell_quest(question)
        return self.questions

    def load(self):
        self.questions = []
        obj = self.fm.file_read_json(self.name_file)
        if not obj is None:
            self.questions = obj
        # else:

        if len(self.questions) == 0:
            self.questions = [
                Question('Сколько будет два плюс два '
                         'умноженное на два?', 6),
                Question(
                    'Бревно нужно распилить на 10 частей, сколько надо сделать распилов',
                    9),
                Question(
                    'На руках 10 пальцев. Сколько пальцев на 5 руках?',
                    25),
                Question(
                    'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
                    60),
                Question(
                    'Пять свечей сгорело, две потухли. Сколько свечей осталось?',
                    2),
                Question(
                    'Ешо один вумный вопрос. Кто ответ знает?',
                    100),
                Question('Cто первый вопрос', 101),
                Question('500', 500)
            ]
        return


    def save(self):
        self.fm.file_write_json(self.name_file, self.get_quest())

    # def save(self):
    #     file_text = ""
    #     for queastion in self.queastions:
    #         file_text = file_text + queastion.to_text()
    #     self.fm.file_write(self.name_file, file_text)

# qs = QuestionStorage()
# qs.save()


class EditQuestionStorage:  # который будеть добавлять удалять вопросы
    def __init__(self):
        self.qs = QuestionStorage()

    def menu(self):
        print("1 = добавить")
        print("2 = Удалить")

        print("10 = печать")
        # print("0 = сохранить")
        m = input()
        if m == "1":
            self.menu_add()
        elif m == "2":
            self.menu_delete()
        elif m == "10":
            self.menu_print()

    def menu_add(self):
        quest = input("вопрос")
        answer = int(input("ответ"))
        self.qs.add_quest(Question(quest, answer))
        self.qs.save()

    def menu_delete(self):
        for i in range(len(self.qs.get_quest())):
            print(i + 1, "--",
                  self.qs.get_quest()[i].to_text())

        num = int(input())
        self.qs.dell_quest_by_index(num - 1)
        self.qs.save()

    def menu_print(self):
        for i in range(len(self.qs.get_quest())):
            print(i + 1, "--",
                  self.qs.get_quest()[i].to_text())

#
# eqs = EditQuestionStorage()
# eqs.menu()
