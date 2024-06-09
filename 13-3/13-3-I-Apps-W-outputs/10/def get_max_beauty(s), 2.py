
def get_max_beauty(s):
    n = len(s)
    beauty = 0
    l, r = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            temp = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            current_beauty = count_beauty(temp)
            if current_beauty > beauty:
                beauty = current_beauty
                l = i + 1
                r = j + 1
    return beauty, l, r

def count_beauty(s):
    n = len(s)
    beauty = 0
    for i in range(n):
        temp = s[i:] + s[:i]
        if is_correct_bracket_sequence(temp):
            beauty += 1
    return beauty

def is_correct_bracket_sequence(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack

n = int(input())
s = input()
beauty, l, r = get_max_beauty(s)
print(beauty)
print(l, r)

