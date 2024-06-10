
def get_common_section(map1, map2):
    # Find the longest common subsequence between the two maps
    lcs = ""
    for i in range(len(map1)):
        for j in range(len(map2[0])):
            if map1[i] == map2[j]:
                lcs += map1[i]
    # Find the starting indices of the lcs in both maps
    i_start = map1.index(lcs[0])
    j_start = map2[0].index(lcs[0])
    return i_start, j_start

def main():
    map1 = []
    map2 = []
    # Read the input
    for _ in range(int(input())):
        map1.append(input())
    for _ in range(int(input())):
        map2.append(input())
    # Find the common section
    i_start, j_start = get_common_section(map1, map2)
    print(i_start, j_start)

if __name__ == '__main__':
    main()

