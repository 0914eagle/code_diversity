
def get_substring(t, k):
    n = len(t)
    s = ""
    for i in range(k):
        s += t
    return s

def solve(t, k):
    n = len(t)
    s = get_substring(t, k)
    return s

if __name__ == '__main__':
    t = input()
    k = int(input())
    print(solve(t, k))

