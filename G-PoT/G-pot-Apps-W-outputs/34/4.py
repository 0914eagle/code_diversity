
def can_form_codeforces(word):
    target = "CODEFORCES"
    n = len(word)
    m = len(target)
    
    for i in range(n):
        for j in range(i, n):
            new_word = word[:i] + word[j+1:]
            if len(new_word) == m and new_word == target:
                return "YES"
    
    return "NO"

word = input().strip()
print(can_form_codeforces(word))
