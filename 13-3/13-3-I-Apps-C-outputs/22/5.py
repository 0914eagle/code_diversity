
def can_obtain_array(a, q):
    n = len(a)
    segments = []
    for i in range(q):
        segments.append((i+1, i+1))
    for i in range(n):
        if a[i] != 0:
            segments[a[i]-1] = (segments[a[i]-1][0], segments[a[i]-1][1], i)
    for i in range(q):
        if segments[i][2] == -1:
            return "NO"
    result = [0] * n
    for i in range(q):
        l, r, pos = segments[i]
        for j in range(l-1, r):
            result[j] = i+1
    return "YES\n" + " ".join(str(x) for x in result)

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    print(can_obtain_array(a, q))

if __name__ == '__main__':
    main()

