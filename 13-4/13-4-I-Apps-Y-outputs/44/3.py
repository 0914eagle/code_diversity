
def is_eastern_gothic(sentence):
    word_list = sentence.split()
    eastern_gothic_words = 0
    for word in word_list:
        if 'ae' in word:
            eastern_gothic_words += 1
    if eastern_gothic_words > len(word_list) * 0.4:
        return True
    else:
        return False

