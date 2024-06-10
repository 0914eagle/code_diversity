
def anti_shuffle(s: str) -> str:
    def sort_word(word):
        return ''.join(sorted(word))

    words = s.split()
    ordered_words = [sort_word(word) for word in words]
    return ' '.join(ordered_words)

if __name__ == "__main__":
    s = input().strip()
    result = anti_shuffle(s)
    print(result)
