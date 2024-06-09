
import re

def get_similarly_spelled_words(text):
    words = re.findall(r"\w+", text)
    similarly_spelled_words = {}
    for word in words:
        core = re.sub(r"[^a-zA-Z]", "", word.lower())
        if core not in similarly_spelled_words:
            similarly_spelled_words[core] = []
        for similar_word in words:
            if core != re.sub(r"[^a-zA-Z]", "", similar_word.lower()):
                continue
            if similar_word not in similarly_spelled_words[core]:
                similarly_spelled_words[core].append(similar_word)
    return similarly_spelled_words

def main():
    text = ""
    while True:
        line = input()
        if line == "***":
            break
        text += line
    similarly_spelled_words = get_similarly_spelled_words(text)
    if not similarly_spelled_words:
        print("***")
    else:
        for core, words in sorted(similarly_spelled_words.items()):
            print(f"{core}: { ' '.join(sorted(set(words))) }")

if __name__ == "__main__":
    main()

