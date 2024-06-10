
def get_participants(n, c):
    participants = []
    for i in range(n):
        participants.append(i+1)
    return participants

def get_first_encounters(n, c):
    first_encounters = []
    for i in range(c):
        a, b, y = map(int, input().split())
        first_encounters.append((a, b, y))
    return first_encounters

def find_year(participants, first_encounters):
    year = 1948
    while year < 2008:
        first_met_before = []
        first_met_after = []
        for participant in participants:
            if (participant[0], participant[1]) in first_encounters:
                if first_encounters[(participant[0], participant[1])] < year:
                    first_met_before.append(participant)
                else:
                    first_met_after.append(participant)
        if len(first_met_before) + len(first_met_after) <= 2*len(participants)/3:
            return year
        year += 1
    return "Impossible"

def main():
    n, c = map(int, input().split())
    participants = get_participants(n, c)
    first_encounters = get_first_encounters(n, c)
    year = find_year(participants, first_encounters)
    print(year)

if __name__ == '__main__':
    main()

