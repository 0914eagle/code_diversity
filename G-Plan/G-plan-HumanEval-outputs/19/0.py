
def anti_shuffle(s: str) -> str:
    def sort_word(word):
        return ''.join(sorted(word))

    result = []
    for word in s.split():
        result.append(sort_word(word))

    return ' '.join(result)

if __name__ == "__main__":
    input_str = input().strip()
    print(anti_shuffle(input_str))
