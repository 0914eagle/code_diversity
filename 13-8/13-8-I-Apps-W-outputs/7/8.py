
def get_possible_options(n, x, y, z, a):
    # Initialize variables
    options = 0
    visited = [False] * n
    queue = [0]
    visited[0] = True
    
    # BFS to find all possible options
    while queue:
        current = queue.pop(0)
        for i in range(n):
            if not visited[i] and a[i] >= x:
                queue.append(i)
                visited[i] = True
                options += 1
    
    return options

def main():
    t = int(input())
    for _ in range(t):
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_possible_options(n, x, y, z, a))

if __name__ == '__main__':
    main()

