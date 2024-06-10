
import re

def split_sentences(S):
    return re.split(r'[.!?]', S)

def is_bored(S):
    sentences = split_sentences(S)
    count = 0
    for sentence in sentences:
        words = sentence.split()
        if words and words[0] == 'I':
            count += 1
    return count

if __name__ == "__main__":
    input_string = input().strip()
    print(is_bored(input_string))
