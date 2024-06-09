
def get_input():
    n, m, s = map(int, input().split())
    people = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))
    shelters = []
    for _ in range(s):
        s, c = map(int, input().split())
        shelters.append((s, c))
    return n, m, s, people, roads, shelters

def solve(n, m, s, people, roads, shelters):
    # create a graph with n locations and m roads
    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    # calculate the shortest distance from each location to each shelter
    dist = [[float('inf') for _ in range(s)] for _ in range(n)]
    for i in range(n):
        for j in range(s):
            dist[i][j] = graph[i][shelters[j][0]-1][1] + shelters[j][1]
    
    # find the minimum time it takes to reach a shelter for each person
    time = [float('inf') for _ in range(n)]
    for i in range(n):
        for j in range(s):
            time[i] = min(time[i], dist[i][j])
    
    # return the maximum time it takes for everyone to reach a shelter
    return max(time)

def main():
    n, m, s, people, roads, shelters = get_input()
    print(solve(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

