
def get_substring(t, k):
    n = len(t)
    s = ""
    for i in range(k):
        s += t
    return s

def get_min_length_string(t, k):
    n = len(t)
    s = ""
    for i in range(k):
        s += t
    return s

if __name__ == '__main__':
    n, k = map(int, input().split())
    t = input()
    s = get_min_length_string(t, k)
    print(s)

