
def get_prettiness(song_title):
    vowels = set("AEIOUY")
    simple_prettiness = 0
    for i in range(len(song_title)):
        for j in range(i, len(song_title) + 1):
            substring = song_title[i:j]
            simple_prettiness += sum(c in vowels for c in substring) / len(substring)
    return simple_prettiness

