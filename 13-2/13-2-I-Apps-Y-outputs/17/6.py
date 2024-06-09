
def get_known_songs(villagers, bard):
    known_songs = set()
    for villager in villagers:
        if villager == bard:
            continue
        known_songs |= villager.known_songs
    return known_songs

def get_villagers_who_know_all_songs(villagers, bard):
    known_songs = get_known_songs(villagers, bard)
    return [villager for villager in villagers if villager.known_songs == known_songs]

class Villager:
    def __init__(self, id, known_songs):
        self.id = id
        self.known_songs = set(known_songs)

    def __repr__(self):
        return f"Villager {self.id}"

if __name__ == '__main__':
    num_villagers = int(input())
    num_evenings = int(input())
    villagers = []
    for i in range(num_villagers):
        known_songs = set(map(int, input().split()))
        villagers.append(Villager(i+1, known_songs))
    bard = villagers[0]
    print(*get_villagers_who_know_all_songs(villagers, bard), sep='\n')

