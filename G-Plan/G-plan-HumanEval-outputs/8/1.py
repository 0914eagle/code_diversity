
import re

def count_boredoms(sentence: str) -> int:
    return 1 if sentence.strip().startswith('I') else 0

def is_bored(S: str) -> int:
    sentences = re.split(r'[.!?]', S)
    return sum(count_boredoms(sentence) for sentence in sentences)

if __name__ == "__main__":
    S = input().strip()
    print(is_bored(S))
