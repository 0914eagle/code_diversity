
def can_obtain_array(a, q):
    n = len(a)
    segments = []
    for i in range(q):
        segments.append((i+1, i+1))
    for i in range(n):
        if a[i] != 0:
            segments[a[i]-1] = (i+1, i+1)
    for i in range(n):
        if segments[i][0] != segments[i][1]:
            return "NO"
    return "YES"

def restore_array(a, q):
    n = len(a)
    segments = []
    for i in range(q):
        segments.append((i+1, i+1))
    for i in range(n):
        if a[i] != 0:
            segments[a[i]-1] = (i+1, i+1)
    result = [0] * n
    for i in range(n):
        result[segments[i][0]-1] = i+1
    return result

if __name__ == '__main__':
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    print(can_obtain_array(a, q))
    if can_obtain_array(a, q) == "YES":
        print(*restore_array(a, q))

