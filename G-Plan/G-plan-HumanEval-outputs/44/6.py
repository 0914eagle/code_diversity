
from collections import Counter

def histogram(test: str):
    def parse_input(test):
        return test.split()

    def count_occurrences(words):
        return Counter(words)

    def find_max_count(occurrences):
        max_count = max(occurrences.values())
        return max_count

    def filter_letters_with_max_count(occurrences, max_count):
        return {letter: count for letter, count in occurrences.items() if count == max_count}

    words = parse_input(test)
    occurrences = count_occurrences(words)
    max_count = find_max_count(occurrences)
    result = filter_letters_with_max_count(occurrences, max_count)
    return result

if __name__ == "__main__":
    test = input().strip()
    result = histogram(test)
    print(result)
