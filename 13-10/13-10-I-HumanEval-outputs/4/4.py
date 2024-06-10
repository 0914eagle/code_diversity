
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    word_dict: Dict[str, int] = {}
    words = test.split(' ')
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    
    return word_dict

if __name__ == '__main__':
    print(histogram("a b c"))
    print(histogram("a b b a"))
    print(histogram("a b c a b"))
    print(histogram("b b b b a"))
    print(histogram(""))

