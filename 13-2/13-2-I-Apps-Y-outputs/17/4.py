
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
    num_villagers, num_evenings = map(int, input().split())
    villagers = [set() for _ in range(num_villagers)]
    for i in range(num_evenings):
        num_present, *present = map(int, input().split())
        for j in range(num_present):
            villagers[present[j]].add(i+1)
    bard = 1
    print(*get_villagers_who_know_all_songs(villagers, bard, range(1, num_evenings+1)), sep='\n')

if __name__ == '__main__':
    main()

