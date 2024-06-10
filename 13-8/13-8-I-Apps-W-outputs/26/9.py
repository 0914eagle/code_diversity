
def align_maps(map1, map2):
    # Find the first row and column where both maps have the same sequence of characters
    for i in range(len(map1)):
        for j in range(len(map2[0])):
            if map1[i] == map2[:,j]:
                return i, j
    return None

def main():
    map1 = input().split()
    map2 = input().split()
    i, j = align_maps(map1, map2)
    print(i, j)

if __name__ == '__main__':
    main()

