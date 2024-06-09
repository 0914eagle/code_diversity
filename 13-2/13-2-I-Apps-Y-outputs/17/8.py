
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
    villagers = [set(map(int, input().split())) for _ in range(num_evenings)]
    bard = 1
    print(*get_villagers_with_all_songs(range(1, num_villagers + 1), bard, villagers), sep='\n')

if __name__ == '__main__':
    main()

