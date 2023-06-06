import re
import random

class Histogram:
    def __init__(self, filename):
        self.histogram = {}
        with open(filename, 'r', encoding="UTF-8") as infile:
            words = infile.read().split()
            for word in words:
                word = re.sub("-", " ", word)
                word = re.sub("[^a-zA-Z]", "", word)
                word = word.lower()
                if self.histogram.get(word):
                    self.histogram[word] += 1
                else:
                    self.histogram[word] = 1

        self.sample_list = self.build_weighted_list()

    def unique_words(self):
        return len(self.histogram.keys())

    def frequency(self, word):
        return self.histogram.get(word, 0)

    def build_weighted_list(self):
        sample_list = []
        for word, number in self.histogram.items():
            for i in range(number):
                sample_list.append(word)

        return sample_list

    def random_word(self):
        return random.choice(list(self.histogram.keys()))

    def weighted_random_word(self):
        return random.choice(self.sample_list)

    def random_sentence(self):
        length = random.randint(10, 25)
        sentence = ""

        for i in range(length):
            sentence += self.weighted_random_word()
            if i == length - 1:
                sentence += "."
            else:
                sentence += " "

        return sentence.capitalize()
