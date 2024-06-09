
def is_tolerable(s, p):
    if len(s) > p:
        return False
    
    for i in range(len(s)):
        if s[i] > chr(ord('a') + p - 1):
            return False
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    
    return True

def next_tolerable(s, p):
    if len(s) == 0:
        return "NO"
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] < chr(ord('z')):
            return s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]
    
    return "NO"

def main():
    n, p = map(int, input().split())
    s = input()
    
    if is_tolerable(s, p):
        print(next_tolerable(s, p))
    else:
        print("NO")

if __name__ == '__main__':
    main()

