
def anti_shuffle(s: str) -> str:
    def order_word(word):
        return ''.join(sorted(word))

    ordered_words = [order_word(word) for word in s.split()]
    return ' '.join(ordered_words)

# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
