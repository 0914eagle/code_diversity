
def get_enemy_spaceships_coordinates(n, m):
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    return y1, y2

def get_max_destroyed_spaceships(y1, y2):
    destroyed_spaceships = 0
    for i in range(len(y1)):
        for j in range(len(y2)):
            if y1[i] == y2[j]:
                destroyed_spaceships += 1
    return destroyed_spaceships

def main():
    n, m = map(int, input().split())
    y1, y2 = get_enemy_spaceships_coordinates(n, m)
    max_destroyed_spaceships = get_max_destroyed_spaceships(y1, y2)
    print(max_destroyed_spaceships)

if __name__ == '__main__':
    main()

