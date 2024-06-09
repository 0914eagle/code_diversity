
def get_closest_vowel(word: str) -> str:
    

    vowels = "aeiouAEIOU"
    word = word[::-1]
    for i, char in enumerate(word):
        if char in vowels:
            if i > 0 and word[i-1] in vowels:
                return ""
            else:
                return char
    return ""

