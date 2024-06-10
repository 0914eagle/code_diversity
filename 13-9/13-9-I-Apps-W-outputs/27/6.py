
def is_reachable(line, k):
    # Initialize variables
    n = len(line)
    start, end = -1, -1
    for i in range(n):
        if line[i] == "G":
            start = i
        elif line[i] == "T":
            end = i
    if start == -1 or end == -1:
        return "NO"
    
    # Check if there is a path from start to end
    visited = [False] * n
    queue = [(start, 0)]
    while queue:
        curr, dist = queue.pop(0)
        if curr == end:
            return "YES"
        for i in range(max(0, curr - k), min(n, curr + k + 1)):
            if line[i] == "." and not visited[i]:
                queue.append((i, dist + 1))
                visited[i] = True
    return "NO"

def main():
    n, k = map(int, input().split())
    line = input()
    print(is_reachable(line, k))

if __name__ == '__main__':
    main()

