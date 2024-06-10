
def get_participants(n, c, encounters):
    participants = set()
    for a, b, y in encounters:
        participants.add(a)
        participants.add(b)
    return participants

def get_first_meeting_year(participants, encounters):
    first_meeting_year = {}
    for a, b, y in encounters:
        if a not in first_meeting_year:
            first_meeting_year[a] = y
        if b not in first_meeting_year:
            first_meeting_year[b] = y
    return first_meeting_year

def divide_participants(participants, first_meeting_year, n):
    part1 = set()
    part2 = set()
    for participant in participants:
        if first_meeting_year[participant] <= n:
            part1.add(participant)
        else:
            part2.add(participant)
    return part1, part2

def get_smallest_year(part1, part2, n):
    smallest_year = n + 1
    for participant in part1:
        if first_meeting_year[participant] < smallest_year:
            smallest_year = first_meeting_year[participant]
    for participant in part2:
        if first_meeting_year[participant] > smallest_year:
            smallest_year = first_meeting_year[participant]
    return smallest_year

def main():
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    participants = get_participants(n, c, encounters)
    first_meeting_year = get_first_meeting_year(participants, encounters)
    part1, part2 = divide_participants(participants, first_meeting_year, n)
    smallest_year = get_smallest_year(part1, part2, n)
    if smallest_year == n + 1:
        print("Impossible")
    else:
        print(smallest_year)

if __name__ == '__main__':
    main()

