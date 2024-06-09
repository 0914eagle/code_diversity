
def is_buildable(s, t):
    if len(s) < len(t):
        return False
    if s == t:
        return True
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            return True
    return False

def main():
    num_cases = int(input())
    for case in range(num_cases):
        s = input()
        t = input()
        if is_buildable(s, t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

