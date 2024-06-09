
def is_buildable(s, t):
    if len(s) < len(t):
        return False
    if s == t:
        return True
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            return True
    return False

def solve(s, t):
    if is_buildable(s, t):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    num_cases = int(input())
    for i in range(num_cases):
        s = input()
        t = input()
        print(solve(s, t))

