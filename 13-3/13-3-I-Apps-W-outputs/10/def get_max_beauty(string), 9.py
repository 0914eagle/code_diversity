
def get_max_beauty(string):
    n = len(string)
    beauty = 0
    l, r = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            s1 = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
            s2 = string[:j] + string[i] + string[j+1:i] + string[j] + string[i+1:]
            beauty = max(beauty, get_beauty(s1), get_beauty(s2))
    return beauty, l, r

def get_beauty(string):
    n = len(string)
    beauty = 0
    for i in range(n):
        s = string[i:] + string[:i]
        if is_correct(s):
            beauty += 1
    return beauty

def is_correct(string):
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack

string = input()
beauty, l, r = get_max_beauty(string)
print(beauty)
print(l, r)

