
def pig_latin(text):
    vowels = "aeiou"
    pig_latin_text = ""
    for word in text.split():
        if word[0] in vowels:
            pig_latin_text += word + "yay "
        else:
            vowel_index = 0
            for i in range(1, len(word)):
                if word[i] in vowels:
                    vowel_index = i
                    break
            pig_latin_text += word[vowel_index:] + word[:vowel_index] + "ay "
    return pig_latin_text.strip()

