
def get_terrain_type(s):
    terrain_type = []
    for c in s:
        if c == 'G':
            terrain_type.append('Grass')
        elif c == 'W':
            terrain_type.append('Water')
        else:
            terrain_type.append('Lava')
    return terrain_type

def get_movement_time(terrain_type, stamina):
    time = 0
    for t in terrain_type:
        if t == 'Grass':
            time += 5
        elif t == 'Water':
            time += 3
        else:
            time += 1
            stamina -= 1
    return time, stamina

def get_shortest_time(terrain_type, stamina):
    time = 0
    for i in range(len(terrain_type)):
        if terrain_type[i] == 'Lava' and stamina == 0:
            return -1
        time, stamina = get_movement_time(terrain_type[i:], stamina)
    return time

def main():
    n = int(input())
    l = list(map(int, input().split()))
    s = input()
    terrain_type = get_terrain_type(s)
    stamina = 0
    time = get_shortest_time(terrain_type, stamina)
    print(time)

if __name__ == '__main__':
    main()

