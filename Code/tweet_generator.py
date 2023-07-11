from parser import Parser
from markov_chain import MarkovChain

class TweetGenerator:
    def __init__(self, source_text):
        self.corpus = Parser(source_text).word_list
        self.markov = MarkovChain(self.corpus)

    def tweet(self):
        tweet = ""
        while len(tweet) < 180:
            tweet += self.markov.generate_sentence()
        return tweet