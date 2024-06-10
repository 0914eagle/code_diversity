
import re

def count_boredoms(sentences):
    count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    return count

def is_bored(S: str) -> int:
    delimiters = ['.', '?', '!']
    sentence = ''
    sentences = []
    for char in S:
        if char in delimiters:
            sentences.append(sentence.strip())
            sentence = ''
        else:
            sentence += char
    if sentence:
        sentences.append(sentence.strip())
    
    return count_boredoms(sentences)

if __name__ == "__main__":
    S = input().strip()
    print(is_bored(S))
