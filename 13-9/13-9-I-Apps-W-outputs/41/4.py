
import random

def generate_essay(A, B):
    vocabulary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    essay = ""
    for i in range(A, B+1):
        essay += random.choice(vocabulary)
    return essay

