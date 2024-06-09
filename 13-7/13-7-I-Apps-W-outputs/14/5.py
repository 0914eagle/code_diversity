
def solve(s):
    n = len(s)
    seen = set()
    queue = [s]
    count = 0
    while queue:
        word = queue.pop(0)
        if word not in seen:
            count += 1
            seen.add(word)
            queue += [word[i:] + word[:i] for i in range(n)]
    return count

