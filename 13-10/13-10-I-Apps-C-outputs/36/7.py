
def get_enemy_spaceships_destructible(x1, y1, x2, y2):
    # Find the number of enemy spaceships that can be destroyed by the laser shots
    destructible_spaceships = 0
    for i in range(len(y1)):
        for j in range(len(y2)):
            if y1[i] == y2[j]:
                destructible_spaceships += 1
    return destructible_spaceships

def main():
    # Read the input
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))

    # Find the largest number of enemy spaceships that can be destroyed
    max_destructible_spaceships = 0
    for i in range(len(y1)):
        for j in range(len(y2)):
            if y1[i] == y2[j]:
                destructible_spaceships = get_enemy_spaceships_destructible(x1, y1, x2, y2)
                if destructible_spaceships > max_destructible_spaceships:
                    max_destructible_spaceships = destructible_spaceships
    print(max_destructible_spaceships)

if __name__ == '__main__':
    main()

