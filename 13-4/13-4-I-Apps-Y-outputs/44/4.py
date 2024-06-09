
def check_east_gotska(sentence):
    words = sentence.split()
    east_gotska_words = 0
    for word in words:
        if 'ae' in word:
            east_gotska_words += 1
    if east_gotska_words >= len(words) * 0.4:
        return "dae ae ju traeligt va"
    else:
        return "haer talar vi rikssvenska"

