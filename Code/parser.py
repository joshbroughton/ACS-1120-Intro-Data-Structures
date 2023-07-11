import re

class Parser:
    def __init__(self, source_text):
        self.word_list = []
        with open(source_text, 'r', encoding="UTF-8") as infile:
            words = infile.read().split()
            for word in words:
                word = re.sub("-", " ", word)
                word = re.sub("[^a-zA-Z!,.?']", "", word)
                if word != "CHAPTER":
                    self.word_list.append(word)

    def word_list(self):
        return self.word_list