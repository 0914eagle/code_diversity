
def get_tea_time(n, l, r):
    tea_time = [0] * n
    queue = []
    for i in range(n):
        queue.append((l[i], r[i], i))
    queue.sort()
    for i in range(n):
        while queue and queue[0][0] <= i:
            tea_time[queue[0][2]] = i + 1
            queue.pop(0)
    return tea_time

def f1(n, l, r):
    return get_tea_time(n, l, r)

def f2(n, l, r):
    return get_tea_time(n, l, r)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = []
        r = []
        for _ in range(n):
            l_i, r_i = map(int, input().split())
            l.append(l_i)
            r.append(r_i)
        print(*f1(n, l, r))
        print(*f2(n, l, r))

