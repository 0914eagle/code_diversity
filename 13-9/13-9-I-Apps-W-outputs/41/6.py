
import random

def generate_essay(A, B):
    essay = ""
    while len(essay) < A:
        word = "".join(random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(random.randint(1, 15)))
        essay += word + " "
    return essay[:B]

