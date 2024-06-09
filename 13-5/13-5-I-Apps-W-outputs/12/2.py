
def can_build_string(s, t):
    if len(s) < len(t):
        return False
    if s == t:
        return True
    for i in range(1, len(s)):
        if s[:i] + s[i+1:] == t:
            return True
    return False

def main():
    num_cases = int(input())
    for case in range(num_cases):
        s = input()
        t = input()
        if can_build_string(s, t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

