
def anti_shuffle(s: str) -> str:
    def ordered_word(word):
        return ''.join(sorted(word))

    words = s.split()
    ordered_words = [ordered_word(word) for word in words]
    return ' '.join(ordered_words)
