
import re

def get_non_similar_keywords(keywords):
    non_similar_keywords = []
    for keyword in keywords:
        if keyword not in non_similar_keywords:
            non_similar_keywords.append(keyword)
    return len(non_similar_keywords)

def main():
    n = int(input())
    keywords = []
    for _ in range(n):
        keyword = input()
        keywords.append(re.sub(r'-', ' ', keyword).lower())
    print(get_non_similar_keywords(keywords))

if __name__ == '__main__':
    main()

