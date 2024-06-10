
def get_common_section(map1, map2):
    # Find the length of the common section
    n = len(map1)
    m = len(map1[0])
    for i in range(n):
        for j in range(m):
            if map1[i][j] != map2[i][j]:
                break
        else:
            continue
        break
    common_section_length = i

    # Find the starting position of the common section
    for j in range(m):
        for i in range(n):
            if map1[i][j] != map2[i][j]:
                break
        else:
            continue
        break
    common_section_start = j

    return common_section_length, common_section_start

def main():
    map1 = []
    map2 = []
    for _ in range(int(input())):
        map1.append(input())
        map2.append(input())
    common_section_length, common_section_start = get_common_section(map1, map2)
    print(common_section_length, common_section_start)

if __name__ == '__main__':
    main()

