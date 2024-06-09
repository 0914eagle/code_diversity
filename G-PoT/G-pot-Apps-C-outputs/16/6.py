
n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]

def min_keystrokes(word):
    min_keystrokes = float('inf')
    for dict_word in dictionary:
        if word.startswith(dict_word):
            keystrokes = len(dict_word) + 1 + len(word) - len(dict_word)
            min_keystrokes = min(min_keystrokes, keystrokes)
    return min_keystrokes

for _ in range(m):
    word_to_type = input()
    print(min_keystrokes(word_to_type))
[/PYTHON