import re

class Parser:
    def __init__(self, source_text):
        self.word_list = []
        with open(source_text, 'r', encoding="UTF-8") as infile:
            text = infile.read()
            words = self.custom_tokenize(text)
            for word in words:
                word = re.sub("[^a-zA-Z0-9,!?.'-]", "", word)
                if word and word != "CHAPTER":
                    self.word_list.append(word)

    def custom_tokenize(self, text):
        # Custom split function to handle whitespace, punctuation, and remove quotations
        return re.findall(r"[\w'-]+|[.,!?]", text)
