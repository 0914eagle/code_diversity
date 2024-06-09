
def reachable_numbers(n):
    visited = set()
    queue = [n]
    count = 0
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            count += 1
            queue += [current // 10, current * 10 + 1]
    return count

