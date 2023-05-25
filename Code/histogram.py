def histogram(filename):
    histogram = {}
    with open(filename, 'r') as infile:
        words = infile.read().split(' ')
        for word in words:
            word = word.strip()
            if histogram.get(word):
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram

def unique_words(histogram):
    return len(histogram.keys())

def frequency(histogram, word):
    return histogram.get(word, 0)

fishgram = histogram('histogram_text.py')
print(fishgram)
print(unique_words(fishgram))
print(frequency(fishgram, 'fish'))
