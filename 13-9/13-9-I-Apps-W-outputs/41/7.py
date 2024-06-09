
import random

def generate_essay(a, b):
    essay = ""
    for i in range(a, b+1):
        essay += random.choice("abcdefghijklmnopqrstuvwxyz ")
    return essay.strip()

