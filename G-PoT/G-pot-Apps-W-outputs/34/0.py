
def check_banner(word):
    target = "CODEFORCES"
    for i in range(len(word)):
        for j in range(i, len(word)):
            new_word = word[:i] + word[j+1:]
            if new_word == target:
                return "YES"
    return "NO"

word = input().strip()
print(check_banner(word))
