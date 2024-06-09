
import re

def check_sentence(sentence):
    words = sentence.split()
    eastern_gothic_words = 0
    for word in words:
        if re.search(r'ae', word):
            eastern_gothic_words += 1
    if eastern_gothic_words >= len(words) * 0.4:
        return "dae ae ju traeligt va"
    else:
        return "haer talar vi rikssvenska"

