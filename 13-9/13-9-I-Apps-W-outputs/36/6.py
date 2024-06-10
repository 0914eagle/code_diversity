
def read_input():
    n, s, t = map(int, input().split())
    p = list(map(int, input().split()))
    return n, s, t, p

def solve(n, s, t, p):
    if s == t:
        return 0
    
    visited = set()
    queue = [(s, 0)]
    while queue:
        position, operations = queue.pop(0)
        if position == t:
            return operations
        if position in visited:
            continue
        visited.add(position)
        for i in range(n):
            new_position = (position - 1) % n + 1
            queue.append((new_position, operations + 1))
    
    return -1

def main():
    n, s, t, p = read_input()
    print(solve(n, s, t, p))

if __name__ == '__main__':
    main()

