
def get_known_songs(villagers, bard):
    known_songs = set()
    for villager in villagers:
        if villager == bard:
            known_songs = set(range(1, len(villagers) + 1))
            break
        else:
            known_songs |= set(villager)
    return known_songs

def get_villagers_with_all_songs(villagers, bard, evenings):
    known_songs = set()
    for evening in evenings:
        known_songs |= get_known_songs(evening, bard)
    return [villager for villager in villagers if villager in known_songs]

def main():
    num_villagers = int(input())
    num_evenings = int(input())
    villagers = []
    for i in range(num_villagers):
        villagers.append(set())
    bard = 0
    for i in range(num_evenings):
        num_present = int(input())
        present = set(map(int, input().split()))
        for villager in present:
            villagers[villager - 1] |= present
        if 1 in present:
            bard = 1
    villagers_with_all_songs = get_villagers_with_all_songs(villagers, bard, evenings)
    print(*villagers_with_all_songs, sep='\n')

if __name__ == '__main__':
    main()

