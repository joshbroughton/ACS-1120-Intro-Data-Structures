import sys
import random

words = sys.argv[1:]
random.shuffle(words)

output = ''

for word in words:
    output += word + ' '

print(output)
