
n, k = map(int, input().split())
videos = []
for i in range(n):
    s, m = map(int, input().split())
    videos.append((s, m))

servers = [0] * k
for i in range(n):
    s, m = videos[i]
    while servers[0] != 0:
        servers.append(servers.pop(0))
    servers[0] = s + m * 60

print(*[s + m * 60 for s, m in videos], sep='\n')

