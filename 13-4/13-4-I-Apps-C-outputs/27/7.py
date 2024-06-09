
import re

def get_similarly_spelled_words(text):
    words = re.findall(r'\w+', text)
    similar_words = {}
    for word in words:
        core = re.sub(r'[^a-zA-Z]', '', word.lower())
        if core not in similar_words:
            similar_words[core] = []
        for similar_word in words:
            if core != re.sub(r'[^a-zA-Z]', '', similar_word.lower()):
                continue
            if core not in similar_words[core] and similar_word != word:
                similar_words[core].append(similar_word)
    return similar_words

def main():
    text = input()
    similar_words = get_similarly_spelled_words(text)
    if not similar_words:
        print("***")
    else:
        for core, words in similar_words.items():
            print(f"{core}: {' '.join(words)}")

if __name__ == "__main__":
    main()

