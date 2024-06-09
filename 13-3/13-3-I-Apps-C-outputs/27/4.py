
def is_verse_pattern_matched(text, verse_pattern):
    vowels = set("aeiouy")
    syllables = []
    for line in text:
        line_syllables = []
        for word in line.split():
            word_syllables = []
            for i in range(len(word)):
                if word[i].lower() in vowels:
                    word_syllables.append(word[i:])
                    break
            if word_syllables:
                line_syllables.extend(word_syllables)
        syllables.append(line_syllables)
    return syllables == verse_pattern

