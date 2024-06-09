
def solve(s):
    n = len(s)
    visited = set()
    queue = [s]
    count = 0
    while queue:
        word = queue.pop(0)
        if word not in visited:
            visited.add(word)
            count += 1
            queue += [word[i:] + word[:i] for i in range(n)]
    return count

