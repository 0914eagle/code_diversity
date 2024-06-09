
n, m = map(int, input().split())
dictionary = [input() for _ in range(n)]

def min_keystrokes(word):
    min_keystrokes = float('inf')
    for i in range(len(word)):
        prefix = word[:i+1]
        for dict_word in dictionary:
            if dict_word.startswith(prefix):
                keystrokes = len(prefix) + 1 + len(word) - len(prefix)
                min_keystrokes = min(min_keystrokes, keystrokes)
                break
    return min_keystrokes

for _ in range(m):
    word = input()
    print(min_keystrokes(word))
