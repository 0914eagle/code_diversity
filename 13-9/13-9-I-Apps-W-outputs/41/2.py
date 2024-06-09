
import random

def generate_essay(A, B):
    essay = ""
    for i in range(A):
        word = ""
        for j in range(random.randint(1, 15)):
            word += chr(random.randint(97, 122))
        essay += word + " "
    return essay[:B]

