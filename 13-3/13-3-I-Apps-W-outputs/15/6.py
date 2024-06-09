
def f1(N, M, map1, map2):
    # Initialize a dictionary to store the counts of each cosmic object type
    cosmic_objects = {}
    for i in range(N):
        for j in range(M):
            cosmic_object = map1[i][j]
            if cosmic_object not in cosmic_objects:
                cosmic_objects[cosmic_object] = 0
            cosmic_objects[cosmic_object] += 1
    
    # Find the cosmic object that appears in both maps the most
    common_cosmic_object = ""
    max_count = 0
    for cosmic_object, count in cosmic_objects.items():
        if count > max_count:
            max_count = count
            common_cosmic_object = cosmic_object
    
    # Find the position of the common cosmic object in both maps
    position1 = []
    position2 = []
    for i in range(N):
        for j in range(M):
            if map1[i][j] == common_cosmic_object:
                position1.append((i, j))
            if map2[i][j] == common_cosmic_object:
                position2.append((i, j))
    
    # Find the intersection of the two lists of positions
    intersection = []
    for pos1 in position1:
        for pos2 in position2:
            if pos1 == pos2:
                intersection.append(pos1)
    
    # Return the first intersection point
    return intersection[0]

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, M = map(int, input().split())
    map1 = [input() for _ in range(N)]
    map2 = [input() for _ in range(M)]
    position = f1(N, M, map1, map2)
    print(position[0], position[1])

