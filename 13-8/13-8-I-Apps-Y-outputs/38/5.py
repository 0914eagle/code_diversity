
def get_substring(t, n, k):
    s = ""
    for i in range(k):
        s += t
    return s

def get_substring_optimized(t, n, k):
    return t * k

if __name__ == '__main__':
    n, k = map(int, input().split())
    t = input()
    print(get_substring_optimized(t, n, k))

