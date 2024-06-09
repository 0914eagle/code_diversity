
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
    known_songs = get_known_songs(villagers, bard)
    return [villager for villager in range(1, len(villagers) + 1) if len(known_songs & set(evenings[villager - 1])) == len(known_songs)]

def main():
    num_villagers, num_evenings = map(int, input().split())
    evenings = [list(map(int, input().split())) for _ in range(num_evenings)]
    bard = 1
    villagers_with_all_songs = get_villagers_with_all_songs(range(1, num_villagers + 1), bard, evenings)
    print(*villagers_with_all_songs, sep='\n')

if __name__ == '__main__':
    main()

