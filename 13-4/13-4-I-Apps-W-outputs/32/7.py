
def read_data():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    return n, k, f, w

def find_s_m(f, w, k):
    s = [0] * len(f)
    m = [0] * len(f)
    for i in range(len(f)):
        if f[i] != -1:
            s[i] = w[i] + s[f[i]]
            m[i] = min(m[f[i]], w[i])
    return s, m

def main():
    n, k, f, w = read_data()
    s, m = find_s_m(f, w, k)
    for i in range(len(f)):
        print(s[i], m[i])

if __name__ == '__main__':
    main()

