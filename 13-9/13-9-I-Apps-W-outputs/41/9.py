
import random

def generate_essay(a, b):
    essay = []
    for i in range(a, b+1):
        word = ''
        for j in range(random.randint(1, 15)):
            word += chr(random.randint(97, 122))
        essay.append(word)
    return ' '.join(essay)

