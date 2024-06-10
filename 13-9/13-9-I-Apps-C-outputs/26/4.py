
def get_number_of_portals(n, portals):
    # Initialize variables
    visited = [False] * (n + 1)
    queue = [1]
    visited[1] = True
    count = 0
    
    # Breadth-first search
    while queue:
        room = queue.pop(0)
        count += 1
        if room == n:
            return count
        for portal in portals:
            if not visited[portal]:
                visited[portal] = True
                queue.append(portal)
    
    return -1

def main():
    n = int(input())
    portals = list(map(int, input().split()))
    print(get_number_of_portals(n, portals) % 1000000007)

if __name__ == '__main__':
    main()

