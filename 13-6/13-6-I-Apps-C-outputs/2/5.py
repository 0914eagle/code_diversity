
def read_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def find_gargoyles(floorplan):
    gargoyles = []
    for i in range(len(floorplan)):
        for j in range(len(floorplan[i])):
            if floorplan[i][j] in "VH":
                gargoyles.append((i, j))
    return gargoyles

def find_mirrors(floorplan):
    mirrors = []
    for i in range(len(floorplan)):
        for j in range(len(floorplan[i])):
            if floorplan[i][j] in "/\\":
                mirrors.append((i, j))
    return mirrors

def find_obstacles(floorplan):
    obstacles = []
    for i in range(len(floorplan)):
        for j in range(len(floorplan[i])):
            if floorplan[i][j] == "#":
                obstacles.append((i, j))
    return obstacles

def find_treasure_door(floorplan):
    for i in range(len(floorplan)):
        for j in range(len(floorplan[i])):
            if floorplan[i][j] == "/":
                return (i, j)
    return None

def find_paths(gargoyles, mirrors, obstacles, treasure_door):
    paths = []
    for gargoyle in gargoyles:
        for mirror in mirrors:
            path = [(gargoyle, mirror)]
            current = (gargoyle, mirror)
            while current != treasure_door:
                next = None
                for neighbor in [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]:
                    if neighbor not in obstacles and neighbor not in paths:
                        next = neighbor
                        break
                if next:
                    path.append(next)
                    current = next
                else:
                    break
            if len(path) > 1:
                paths.append(path)
    return paths

def rotate_gargoyle(gargoyle, mirror):
    if gargoyle[1] == mirror[1]:
        return (gargoyle[0], gargoyle[1] + 1)
    else:
        return (gargoyle[0] + 1, gargoyle[1])

def solve_puzzle(n, m, floorplan):
    gargoyles = find_gargoyles(floorplan)
    mirrors = find_mirrors(floorplan)
    obstacles = find_obstacles(floorplan)
    treasure_door = find_treasure_door(floorplan)
    paths = find_paths(gargoyles, mirrors, obstacles, treasure_door)
    min_gargoyles = len(paths)
    for path in paths:
        rotated_gargoyles = set()
        for i in range(len(path)-1):
            gargoyle = path[i]
            mirror = path[i+1]
            if gargoyle not in rotated_gargoyles:
                rotated_gargoyles.add(gargoyle)
                rotated_gargoyle = rotate_gargoyle(gargoyle, mirror)
                if rotated_gargoyle not in rotated_gargoyles:
                    rotated_gargoyles.add(rotated_gargoyle)
        if len(rotated_gargoyles) < min_gargoyles:
            min_gargoyles = len(rotated_gargoyles)
    return min_gargoyles

def main():
    n, m, floorplan = read_input()
    print(solve_puzzle(n, m, floorplan))

if __name__ == '__main__':
    main()

