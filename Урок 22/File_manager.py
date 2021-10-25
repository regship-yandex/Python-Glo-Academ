import os.path
import jsonpickle
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

