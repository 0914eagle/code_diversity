
def read_input():
    n, k = map(int, input().split())
    line = input()
    return n, k, line

def find_grasshopper(line, k):
    for i in range(len(line)):
        if line[i] == 'G':
            return i
    return -1

def find_insect(line, k):
    for i in range(len(line)):
        if line[i] == 'T':
            return i
    return -1

def can_jump(i, j, k):
    return abs(i - j) <= k

def solve(n, k, line):
    grasshopper = find_grasshopper(line, k)
    insect = find_insect(line, k)
    if grasshopper == -1 or insect == -1:
        return "NO"
    visited = [False] * n
    queue = [(grasshopper, 0)]
    while queue:
        current, steps = queue.pop(0)
        if current == insect:
            return "YES"
        for i in range(current - k, current + k + 1):
            if can_jump(current, i, k) and not visited[i] and line[i] == '.':
                visited[i] = True
                queue.append((i, steps + 1))
    return "NO"

def main():
    n, k, line = read_input()
    print(solve(n, k, line))

if __name__ == '__main__':
    main()

