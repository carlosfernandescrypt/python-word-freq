import string
from collections import defaultdict

word_freq = defaultdict(int)

with open('input.txt', 'r') as f:
    for line in f:
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words = line.split()
        for word in words:
            word_freq[word] += 1

for word, freq in word_freq.items():
    print(f'{word}: {freq}')
