
n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]
words_to_type = [input() for _ in range(m)]

def min_keystrokes(word):
    min_keystrokes = float('inf')
    for dict_word in dictionary:
        if word.startswith(dict_word):
            keystrokes = len(dict_word) + 1 + len(word) - len(dict_word)
            min_keystrokes = min(min_keystrokes, keystrokes)
    return min_keystrokes

for word in words_to_type:
    print(min_keystrokes(word))
[/PYTHON