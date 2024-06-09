
def anti_shuffle(s: str) -> str:
    def ordered_word(word):
        return ''.join(sorted(word))

    result = []
    current_word = []
    for char in s:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                result.append(ordered_word(''.join(current_word)))
                current_word = []
            result.append(char)

    if current_word:
        result.append(ordered_word(''.join(current_word)))

    return ''.join(result)

# Test cases
print(anti_shuffle('Hi'))  # 'Hi'
print(anti_shuffle('hello'))  # 'ehllo'
print(anti_shuffle('Hello World!!!'))  # 'Hello !!!Wdlor'
