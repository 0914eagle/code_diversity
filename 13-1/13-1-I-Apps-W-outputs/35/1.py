
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

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = [0] * n
        r = [0] * n
        for i in range(n):
            l[i], r[i] = map(int, input().split())
        tea_time = get_tea_time(n, l, r)
        print(*tea_time)

if __name__ == '__main__':
    main()

