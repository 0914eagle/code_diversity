
def anti_shuffle(s: str) -> str:
    
    words = s.split()
    ordered_words = []
    for word in words:
        ordered_words.append("".join(sorted(word)))
    return " ".join(ordered_words)

