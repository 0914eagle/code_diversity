
def get_possible_chests(chests, keys):
    possible_chests = []
    for i, chest in enumerate(chests):
        for j, key in enumerate(keys):
            if (chest + key) % 2 == 1:
                possible_chests.append((i, j))
    return possible_chests

def get_max_chests(possible_chests):
    max_chests = 0
    for i in range(len(possible_chests)):
        for j in range(i+1, len(possible_chests)):
            if possible_chests[i][0] != possible_chests[j][0] and possible_chests[i][1] != possible_chests[j][1]:
                max_chests = max(max_chests, i+j+1)
    return max_chests

def main():
    n, m = map(int, input().split())
    chests = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    possible_chests = get_possible_chests(chests, keys)
    max_chests = get_max_chests(possible_chests)
    print(max_chests)

if __name__ == '__main__':
    main()

