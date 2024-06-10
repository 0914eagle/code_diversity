
def solve(n, k, t):
    # find the length of the smallest substring that contains t
    min_len = len(t)
    for i in range(len(t)):
        if t[i:] == t[:len(t)-i]:
            min_len = min(min_len, len(t)-i)
    
    # construct the answer string
    s = ""
    for i in range(k):
        s += t[:min_len]
    
    return s

def main():
    n, k = map(int, input().split())
    t = input()
    print(solve(n, k, t))

if __name__ == '__main__':
    main()

