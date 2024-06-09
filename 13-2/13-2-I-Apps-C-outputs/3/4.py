
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
    
    s = list(s)
    i = len(s) - 1
    while i >= 0 and s[i] == chr(ord('z') - p + 1):
        i -= 1
    
    if i == -1:
        return "NO"
    
    s[i] = chr(ord(s[i]) + 1)
    for j in range(i + 1, len(s)):
        s[j] = chr(ord('a') + p - 1)
    
    return "".join(s)

def main():
    n, p = map(int, input().split())
    s = input()
    if is_tolerable(s, p):
        print(find_next_tolerable(s, p))
    else:
        print("NO")

if __name__ == '__main__':
    main()

