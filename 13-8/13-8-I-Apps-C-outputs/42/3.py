
import sys
input = sys.stdin.read()
n, k = map(int, input.split('\n')[0].split())
courses = {}
for line in input.split('\n')[1:]:
    name, diff = line.split()
    if name not in courses:
        courses[name] = []
    courses[name].append(int(diff))

def dfs(i, visited, level, total):
    if i == k:
        return total
    visited.add(i)
    for j in range(1, n+1):
        if j not in visited and len(courses[j]) > level:
            total = min(total, dfs(i+1, visited, level+1, total+courses[j][level]))
    visited.remove(i)
    return total

def solve(k):
    visited = set()
    return dfs(0, visited, 0, 0)

if __name__ == '__main__':
    print(solve(k))

