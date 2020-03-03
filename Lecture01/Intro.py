import sys

freq = {}  # frequency of words in text
for word in input().split(" "):
    freq[word] = 1 + freq.get(word, 0)
print(freq)
