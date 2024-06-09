
def is_east_gothic(sentence):
    word_list = sentence.split()
    east_gothic_words = 0
    for word in word_list:
        if 'ae' in word:
            east_gothic_words += 1
    if east_gothic_words > len(word_list) * 0.4:
        return True
    else:
        return False

