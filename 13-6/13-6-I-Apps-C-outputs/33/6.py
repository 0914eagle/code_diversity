
def get_badge_numbers(start, end, locks):
    visited = set()
    queue = [(start, 0)]
    while queue:
        room, count = queue.pop(0)
        if room == end:
            return count
        if room in visited:
            continue
        visited.add(room)
        for lock in locks:
            if lock[0] == room:
                queue.append((lock[1], count + 1))
    return 0

