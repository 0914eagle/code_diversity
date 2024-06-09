
def can_form_codeforces(word):
    target = "CODEFORCES"
    n = len(word)
    m = len(target)
    
    for i in range(n):
        for j in range(i, n):
            if word[:i] + word[j+1:] == target:
                return "YES"
    
    return "NO"

word = input().strip()
print(can_form_codeforces(word))
