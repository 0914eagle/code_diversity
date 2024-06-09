
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    translated_text = ""
    for word in words:
        if word[0] in vowels:
            translated_word = word + "yay"
        else:
            vowel_index = 0
            for i in range(1, len(word)):
                if word[i] in vowels:
                    vowel_index = i
                    break
            translated_word = word[vowel_index:] + word[:vowel_index] + "ay"
        translated_text += translated_word + " "
    return translated_text.strip()

