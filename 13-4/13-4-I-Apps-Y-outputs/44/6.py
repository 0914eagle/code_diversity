
def check_east_gothic(sentence):
    words = sentence.split()
    east_gothic_words = 0
    for word in words:
        if 'ae' in word:
            east_gothic_words += 1
    if east_gothic_words >= len(words) * 0.4:
        return "dae ae ju traeligt va"
    else:
        return "haer talar vi rikssvenska"

