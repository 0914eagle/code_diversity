
def is_verse_pattern_matched(text, verse_pattern):
    n = len(text)
    if len(verse_pattern) != n:
        return "NO"
    for i in range(n):
        line = text[i]
        syllables = 0
        for word in line.split():
            if any(c in "aeiouy" for c in word):
                syllables += 1
        if syllables != verse_pattern[i]:
            return "NO"
    return "YES"

