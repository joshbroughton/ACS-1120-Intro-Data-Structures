import sys
from random import sample
import time

start_time = time.time()

num_of_words = int(sys.argv[1])
words = None


with open('/usr/share/dict/words', 'r') as dictionary:
    words = dictionary.readlines()

words_sample = sample(words, num_of_words)
output = ''

for word in words_sample:
    output += word.strip() + ' '

print(output)

end_time = time.time()

elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time}')
