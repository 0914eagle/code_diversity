
def get_shortest_path_length(dists, s, t):
    n = len(dists)
    dists.append(dists[0])
    dists.insert(0, dists[n-1])
    dists[s-1] = 0
    for i in range(n-1):
        for j in range(n):
            dists[j] = min(dists[j], dists[j-1] + dists[j])
    return dists[t-1]

def main():
    n, s, t = map(int, input().split())
    dists = list(map(int, input().split()))
    print(get_shortest_path_length(dists, s, t))

if __name__ == '__main__':
    main()

