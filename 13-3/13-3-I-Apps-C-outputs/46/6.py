
def get_badge_numbers(start, end, locks):
    visited = set()
    queue = [(start, 0)]
    while queue:
        room, badge = queue.pop(0)
        if room == end:
            return badge
        for lock in locks:
            if lock[0] == room and lock[1] not in visited:
                queue.append((lock[1], badge | lock[2]))
                visited.add(lock[1])
    return 0

def main():
    n, l, b = map(int, input().split())
    s, d = map(int, input().split())
    locks = []
    for i in range(l):
        a, b, x, y = map(int, input().split())
        locks.append((a, b, x, y))
    print(get_badge_numbers(s, d, locks))

if __name__ == "__main__":
    main()

