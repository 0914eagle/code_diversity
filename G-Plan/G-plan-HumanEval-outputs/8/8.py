
import re

def count_boredoms(sentences):
    count = 0
    for sentence in sentences:
        if sentence.startswith("I"):
            count += 1
    return count

def is_bored(S: str) -> int:
    sentences = re.split(r'[.!?]', S)
    return count_boredoms(sentences)

if __name__ == "__main__":
    input_string = input().strip()
    print(is_bored(input_string))
