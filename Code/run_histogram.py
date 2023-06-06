from histogram import Histogram

hist = Histogram('bread.txt')
print(hist.unique_words())
print(hist.histogram)

# test roughly equal distribution of words when no weighting
count = 0
words = {}
hist.build_weighted_list()

while count < 10000:
    count += 1
    word = hist.weighted_random_word()
    if words.get(word):
        words[word] += 1
    else:
        words[word] = 1

print(hist.random_sentence())
