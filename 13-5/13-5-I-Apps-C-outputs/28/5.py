
def get_input():
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    return n, m, y1, y2

def get_possible_positions(n, m, y1, y2):
    positions = []
    for i in range(n):
        for j in range(m):
            if y1[i] == y2[j]:
                positions.append((0, y1[i]))
    return positions

def get_destroyed_spaceships(positions, y1, y2):
    destroyed = 0
    for i in range(len(y1)):
        for j in range(len(y2)):
            if y1[i] == y2[j] and positions[i][1] == positions[j][1]:
                destroyed += 1
    return destroyed

def main():
    n, m, y1, y2 = get_input()
    positions = get_possible_positions(n, m, y1, y2)
    destroyed = get_destroyed_spaceships(positions, y1, y2)
    print(destroyed)

if __name__ == '__main__':
    main()

