
def get_tshirt_sizes():
    tshirt_sizes = input().split()
    return [int(size) for size in tshirt_sizes]

def get_participants():
    n = int(input())
    participants = []
    for i in range(n):
        size = input()
        if ',' in size:
            sizes = size.split(',')
            participants.append((int(sizes[0]), int(sizes[1])))
        else:
            participants.append((int(size),))
    return participants

def is_valid_distribution(participants, tshirt_sizes):
    for size in participants:
        if size in tshirt_sizes:
            tshirt_sizes.remove(size)
        elif size[0] in tshirt_sizes and size[1] in tshirt_sizes:
            tshirt_sizes.remove(size[0])
            tshirt_sizes.remove(size[1])
        else:
            return False
    return True

def get_valid_distribution(participants, tshirt_sizes):
    for i in range(len(participants)):
        if participants[i] in tshirt_sizes:
            tshirt_sizes.remove(participants[i])
        elif participants[i][0] in tshirt_sizes and participants[i][1] in tshirt_sizes:
            tshirt_sizes.remove(participants[i][0])
            tshirt_sizes.remove(participants[i][1])
        else:
            return False
    return True

def main():
    tshirt_sizes = get_tshirt_sizes()
    participants = get_participants()
    if is_valid_distribution(participants, tshirt_sizes):
        print('YES')
        for participant in participants:
            if participant in tshirt_sizes:
                print(participant)
            else:
                print(participant[0])
    else:
        print('NO')

if __name__ == '__main__':
    main()

