
def get_intersection(map1, map2):
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                return i, j
    return None

def main():
    map1 = []
    map2 = []
    for _ in range(int(input())):
        map1.append(input())
        map2.append(input())
    intersection = get_intersection(map1, map2)
    print(intersection[0], intersection[1])

if __name__ == '__main__':
    main()

