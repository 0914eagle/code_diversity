
def get_shirt_sizes(num_shirts):
    return list(map(int, input().split()))

def get_participants():
    n = int(input())
    participants = []
    for _ in range(n):
        participants.append(input())
    return participants

def is_valid_distribution(shirt_sizes, participants):
    shirt_sizes = shirt_sizes[:]
    for participant in participants:
        if ',' in participant:
            sizes = participant.split(',')
            if shirt_sizes[sizes[0]] == 0 or shirt_sizes[sizes[1]] == 0:
                return False
            shirt_sizes[sizes[0]] -= 1
            shirt_sizes[sizes[1]] -= 1
        else:
            if shirt_sizes[participant] == 0:
                return False
            shirt_sizes[participant] -= 1
    return True

def find_valid_distribution(shirt_sizes, participants):
    shirt_sizes = shirt_sizes[:]
    for participant in participants:
        if ',' in participant:
            sizes = participant.split(',')
            shirt_sizes[sizes[0]] -= 1
            shirt_sizes[sizes[1]] -= 1
        else:
            shirt_sizes[participant] -= 1
    return shirt_sizes

def main():
    shirt_sizes = get_shirt_sizes(6)
    participants = get_participants()
    if is_valid_distribution(shirt_sizes, participants):
        print('YES')
        shirt_sizes = find_valid_distribution(shirt_sizes, participants)
        for participant in participants:
            print(participant)
    else:
        print('NO')

if __name__ == '__main__':
    main()

