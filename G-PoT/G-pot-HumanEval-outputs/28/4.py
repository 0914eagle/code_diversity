
def anti_shuffle(s: str) -> str:
    ordered_words = []
    for word in s.split():
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    
    return ' '.join(ordered_words)
