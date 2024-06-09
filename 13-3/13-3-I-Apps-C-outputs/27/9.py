
def is_verse_pattern_matched(text, verse_pattern):
    n = len(text)
    if len(verse_pattern) != n:
        return "NO"
    for i in range(n):
        line = text[i]
        syllables = []
        for word in line.split():
            if any(c in "aeiouy" for c in word):
                syllables += [word[j:j+1] for j in range(len(word))]
        if len(syllables) != verse_pattern[i]:
            return "NO"
    return "YES"

