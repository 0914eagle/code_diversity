
def get_reachable_districts(n, a):
    
    reachable_districts = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                reachable_districts.append([i, j])
    return reachable_districts

def get_possible_roads(reachable_districts):
    
    possible_roads = []
    for i in range(len(reachable_districts)):
        for j in range(i+1, len(reachable_districts)):
            if reachable_districts[i][0] != reachable_districts[j][0] and reachable_districts[i][1] != reachable_districts[j][1]:
                possible_roads.append([reachable_districts[i][0], reachable_districts[j][1]])
    return possible_roads

def get_final_roads(possible_roads, n):
    
    final_roads = []
    for i in range(n-1):
        for j in range(i+1, n):
            if [i, j] in possible_roads:
                final_roads.append([i, j])
                break
    return final_roads

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        reachable_districts = get_reachable_districts(n, a)
        possible_roads = get_possible_roads(reachable_districts)
        final_roads = get_final_roads(possible_roads, n)
        if len(final_roads) == n-1:
            print("YES")
            for road in final_roads:
                print(*road)
        else:
            print("NO")

if __name__ == '__main__':
    main()

