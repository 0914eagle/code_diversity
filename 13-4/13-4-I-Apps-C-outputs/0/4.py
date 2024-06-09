
def is_tolerable(s, p):
    if len(s) > p:
        return False
    
    for i in range(len(s)):
        if s[i] > chr(ord('a') + p - 1):
            return False
    
    for i in range(len(s) - 1):
        if s[i] == s[len(s) - i - 1]:
            return False
    
    return True

def find_next_tolerable(s, p):
    if len(s) == 0:
        return "NO"
    
    next_s = ""
    for i in range(len(s)):
        if s[i] == chr(ord('z')):
            next_s += "a"
        else:
            next_s += chr(ord(s[i]) + 1)
    
    if is_tolerable(next_s, p):
        return next_s
    else:
        return "NO"

if __name__ == '__main__':
    n, p = map(int, input().split())
    s = input()
    print(find_next_tolerable(s, p))

