class User:

    def __init__(self, name="нет имени",
                 count_right_answer=0, result="тест не пройден"):
        self.name = name
        self.count_right_answer = count_right_answer
        self.result = result

    def count_correct_answer(self):
        self.count_right_answer += 1

    def to_text(self):
        return f'{self.name};{self.count_right_answer};{self.result}\n'

    def load(self, str):
        str_split = str.split(";")
        if len(str_split) == 3:
            self.name = str_split[0]
            self.count_right_answer = int(str_split[1])
            self.result = str_split[2]

    def __str__(self):
        return self.to_text()
