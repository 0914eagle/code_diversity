
def get_badge_numbers(start, end, locks):
    visited = set()
    queue = [(start, 0)]
    while queue:
        room, badge = queue.pop(0)
        if room == end:
            return badge
        for lock in locks[room]:
            if lock[0] <= badge <= lock[1] and lock[2] not in visited:
                visited.add(lock[2])
                queue.append((lock[2], badge))
    return 0

def main():
    num_rooms, num_locks, num_badges = map(int, input().split())
    start, end = map(int, input().split())
    locks = [[] for _ in range(num_rooms + 1)]
    for _ in range(num_locks):
        a, b, x, y = map(int, input().split())
        locks[a].append((x, y, b))
    print(get_badge_numbers(start, end, locks))

if __name__ == "__main__":
    main()

