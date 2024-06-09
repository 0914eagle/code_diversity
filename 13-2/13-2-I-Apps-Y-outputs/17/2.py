
def get_known_songs(villagers, bard):
    known_songs = set()
    for villager in villagers:
        if villager == bard:
            known_songs.add(villager)
        else:
            known_songs.update(villager)
    return known_songs

def get_villagers_who_know_all_songs(villagers, bard, evenings):
    known_songs = set()
    for evening in evenings:
        known_songs.update(get_known_songs(evening, bard))
    return [villager for villager in villagers if villager in known_songs]

def main():
    num_villagers = int(input())
    num_evenings = int(input())
    villagers = [set() for _ in range(num_villagers)]
    bard = 0
    for i in range(num_evenings):
        num_present = int(input())
        present = set(map(int, input().split()))
        for villager in present:
            villagers[villager].update(present)
        if bard in present:
            bard = villager
    print(*get_villagers_who_know_all_songs(villagers, bard, evenings), sep='\n')

if __name__ == '__main__':
    main()

