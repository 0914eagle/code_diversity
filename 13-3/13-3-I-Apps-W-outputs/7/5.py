
n, k = map(int, input().split())
videos = []
for i in range(n):
    s, m = map(int, input().split())
    videos.append((s, m))

servers = [0] * k
current_time = 0
result = []

for video in videos:
    while servers.count(0) == 0:
        current_time += 1
        for i in range(k):
            if servers[i] > 0:
                servers[i] -= 1
    servers[servers.index(0)] = video[1]
    result.append(current_time + video[1])

print(*result, sep='\n')

