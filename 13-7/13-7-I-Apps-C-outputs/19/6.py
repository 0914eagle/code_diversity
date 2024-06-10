
def get_participants_first_encounter(c, participants):
    first_encounter = {}
    for i in range(c):
        a, b, y = map(int, input().split())
        if a not in first_encounter:
            first_encounter[a] = []
        first_encounter[a].append((b, y))
    return first_encounter

def divide_participants(n, c, first_encounter):
    participants = set(range(1, n + 1))
    part1 = set()
    part2 = set()
    for i in range(c):
        a, b, y = first_encounter[i]
        if y <= 1987:
            part1.add(a)
            part1.add(b)
        else:
            part2.add(a)
            part2.add(b)
        participants.remove(a)
        participants.remove(b)
    if len(part1) + len(part2) > 2 * n // 3:
        return "Impossible"
    return "Possible"

def main():
    n, c = map(int, input().split())
    first_encounter = get_participants_first_encounter(c, participants)
    print(divide_participants(n, c, first_encounter))

if __name__ == '__main__':
    main()

