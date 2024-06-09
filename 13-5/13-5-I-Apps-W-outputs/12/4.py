
def can_build_string(s, t):
    if len(s) < len(t):
        return False
    if s == t:
        return True
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            return True
    return False

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        s = input()
        t = input()
        if can_build_string(s, t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

