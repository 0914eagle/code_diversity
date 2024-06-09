
n, k = map(int, input().split())
videos = []
for i in range(n):
    s, m = map(int, input().split())
    videos.append((s, m))

servers = [0] * k
for i in range(n):
    s, m = videos[i]
    while servers[0] > s:
        servers.pop(0)
    servers.append(s + m * 60)

print(*servers, sep='\n')

