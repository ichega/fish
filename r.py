import os

words = open('names.txt', 'r').read()
words = words.replace(" ", "")

print(words)
words = words.split(',')
with open('names.txt', 'w') as f:
    f.write("\n".join(words))


