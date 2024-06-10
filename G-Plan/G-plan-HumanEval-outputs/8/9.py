
import re

def split_sentences(S):
    return re.split(r'[.!?]', S)

def is_bored(S):
    sentences = split_sentences(S)
    count = 0
    for sentence in sentences:
        if sentence.strip().startswith('I'):
            count += 1
    return count

if __name__ == "__main__":
    S = input().strip()
    print(is_bored(S))
