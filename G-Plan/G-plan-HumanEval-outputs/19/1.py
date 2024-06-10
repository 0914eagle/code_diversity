
def anti_shuffle(s: str) -> str:
    def sort_word(word):
        return ''.join(sorted(word))

    ordered_words = [sort_word(word) for word in s.split()]
    return ' '.join(ordered_words)

if __name__ == "__main__":
    input_string = input().strip()
    result = anti_shuffle(input_string)
    print(result)
