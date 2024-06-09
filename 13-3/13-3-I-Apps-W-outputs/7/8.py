
n, k = map(int, input().split())
videos = []
for i in range(n):
    s, m = map(int, input().split())
    videos.append((s, m))

servers = [0] * k
current_time = 0
result = []

while videos or servers:
    if videos and servers.count(0) > 0:
        video = videos.pop(0)
        server = servers.index(0)
        servers[server] = video[1] * 60
        result.append(current_time + video[0])
    else:
        current_time += 1
        for i in range(k):
            if servers[i] > 0:
                servers[i] -= 1
            if servers[i] == 0 and videos:
                video = videos.pop(0)
                servers[i] = video[1] * 60
                result.append(current_time + video[0])

for i in result:
    print(i)

