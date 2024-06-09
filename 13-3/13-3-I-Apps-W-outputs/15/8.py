
def find_overlapping_section(map1, map2):
    for i in range(len(map1)):
        for j in range(len(map2[0])):
            if map1[i] == map2[j]:
                return i, j
    return None

