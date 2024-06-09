
def read_input():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(list(input()))
    return H, W, S

def find_start_goal(H, W, S):
    start, goal = None, None
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                if start is None:
                    start = (i, j)
                elif goal is None:
                    goal = (i, j)
                    break
    return start, goal

def bfs(H, W, S, start, goal):
    queue = [(start, 0)]
    visited = set()
    while queue:
        current, distance = queue.pop(0)
        if current == goal:
            return distance
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = current[0] + i, current[1] + j
            if 0 <= new_i < H and 0 <= new_j < W and S[new_i][new_j] == "." and (new_i, new_j) not in visited:
                queue.append(((new_i, new_j), distance + 1))
                visited.add((new_i, new_j))
    return -1

def solve(H, W, S):
    start, goal = find_start_goal(H, W, S)
    return bfs(H, W, S, start, goal)

if __name__ == '__main__':
    H, W, S = read_input()
    print(solve(H, W, S))

