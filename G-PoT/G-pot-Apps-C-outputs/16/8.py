
n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]
words_to_type = [input() for _ in range(m)]

word_dict = {word: i for i, word in enumerate(dictionary)}

for word in words_to_type:
    min_keystrokes = float('inf')
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in word_dict:
            keystrokes = len(prefix) + 1 + len(word) - i
            min_keystrokes = min(min_keystrokes, keystrokes)
    print(min_keystrokes)
