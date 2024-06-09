
def is_eastern_gothic(sentence):
    word_list = sentence.split()
    eastern_gothic_words = 0
    for word in word_list:
        if 'ae' in word:
            eastern_gothic_words += 1
    if eastern_gothic_words / len(word_list) >= 0.4:
        return True
    else:
        return False

def main():
    sentence = input()
    if is_eastern_gothic(sentence):
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

if __name__ == "__main__":
    main()

