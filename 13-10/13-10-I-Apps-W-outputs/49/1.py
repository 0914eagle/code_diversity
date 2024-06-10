
def get_shirt_sizes():
    return list(map(int, input().split()))

def get_participants():
    return int(input())

def get_participant_sizes():
    participant_sizes = []
    for _ in range(get_participants()):
        sizes = input().split(',')
        if len(sizes) == 1:
            participant_sizes.append(sizes[0])
        else:
            participant_sizes.append((sizes[0], sizes[1]))
    return participant_sizes

def is_valid_distribution(t_shirt_sizes, participant_sizes):
    for size in participant_sizes:
        if size in t_shirt_sizes:
            t_shirt_sizes.remove(size)
        elif size[0] in t_shirt_sizes and size[1] in t_shirt_sizes:
            t_shirt_sizes.remove(size[0])
            t_shirt_sizes.remove(size[1])
        else:
            return False
    return True

def find_distribution(t_shirt_sizes, participant_sizes):
    for size in participant_sizes:
        if size in t_shirt_sizes:
            t_shirt_sizes.remove(size)
        elif size[0] in t_shirt_sizes and size[1] in t_shirt_sizes:
            t_shirt_sizes.remove(size[0])
            t_shirt_sizes.remove(size[1])
        else:
            return None
    return t_shirt_sizes

def main():
    t_shirt_sizes = get_shirt_sizes()
    participant_sizes = get_participant_sizes()
    if is_valid_distribution(t_shirt_sizes, participant_sizes):
        print('YES')
        for size in find_distribution(t_shirt_sizes, participant_sizes):
            print(size)
    else:
        print('NO')

if __name__ == '__main__':
    main()

