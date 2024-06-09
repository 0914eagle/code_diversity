
def get_prettiness(song_title):
    vowels = set("AEIOUY")
    simple_prettiness = 0
    for i in range(len(song_title)):
        for j in range(i, len(song_title) + 1):
            substring = song_title[i:j]
            simple_prettiness += len([c for c in substring if c in vowels]) / len(substring)
    return simple_prettiness

