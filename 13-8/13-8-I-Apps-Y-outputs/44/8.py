
def get_platforms(n, m, c):
    platforms = []
    for i in range(m):
        platforms.append([(n+1)*i//m, (n+1)*(i+1)//m-1])
    return platforms

def can_reach(n, m, d, c, platforms):
    visited = [False] * (n+2)
    queue = [(0, 0)]
    while queue:
        pos, dist = queue.pop(0)
        if pos == n+1:
            return True
        if dist > d:
            continue
        for i in range(m):
            if platforms[i][0] <= pos <= platforms[i][1]:
                for j in range(max(0, pos-d), min(n+1, pos+d+1)):
                    if not visited[j] and j != pos:
                        queue.append((j, dist+1))
                        visited[j] = True
    return False

def main():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    platforms = get_platforms(n, m, c)
    if can_reach(n, m, d, c, platforms):
        print("YES")
        a = [0] * (n+2)
        for i in range(m):
            for j in range(platforms[i][0], platforms[i][1]+1):
                a[j] = i+1
        print(" ".join(map(str, a[1:-1])))
    else:
        print("NO")

if __name__ == '__main__':
    main()

