import random

from listogram import Listogram

class MarkovChain(dict):
    """MarkovChain is a dictionary mapping words in a corpus to a histogram of the words
    that follow that word in the coprus"""
    def __init__(self, word_list=None):
        """Initialize the markovchain as a dictogram, build the markov chain"""
        super().__init__()
        # build a dict of lists, where the key is a word, and value is a list of tokens which
        # occur after that word in the corpus
        if word_list is not None:
            for i, word in enumerate(word_list):
                if i <= (len(word_list) - 2):
                    self.build_sublists(word, word_list[i + 1])
                else:
                    if word not in self:
                        self[word] = []
        # iterate over the keys, and build frequency histograms for them
        for word, tokens in self.items():
            self[word] = Listogram(tokens)

        print(self)

    def build_sublists(self, word, next_word):
        '''helper method to build the sublists during construction'''
        if word in self:
            self[word].append(next_word)
        else:
            self[word] = [next_word]

    def generate_sentence(self):
        '''Generate a sentece; hardcoding the start for now'''
        length = random.randint(10, 25)
        last_word = "A"
        sentence = "A"

        for i in range(length):
            if self[last_word]:
                next_word = self[last_word].sample()
                sentence += " " + next_word
                last_word = next_word

        return sentence


markov = MarkovChain(['A', 'man', 'a', 'plan', 'a', 'canal:', 'Panama!', 'A', 'dog', 'a', 'panic', 'in', 'a', 'pagoda!'])
print(markov.generate_sentence())
