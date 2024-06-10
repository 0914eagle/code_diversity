
def find_common_section(map1, map2):
    # Initialize a 2D array to store the count of common objects in each section
    common_count = [[0] * len(map2[0]) for _ in range(len(map1))]

    # Loop through each section of map1 and count the number of common objects with map2
    for i in range(len(map1)):
        for j in range(len(map2[0])):
            for k in range(len(map2)):
                if map1[i][j] == map2[k][j]:
                    common_count[i][j] += 1

    # Find the maximum number of common objects in any section
    max_common = max(max(row) for row in common_count)

    # Return the row and column indices of the section with the maximum number of common objects
    return [i + 1 for i, row in enumerate(common_count) if max(row) == max_common][0], [j + 1 for j, col in enumerate(common_count[0]) if col == max_common][0]

def main():
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    print(*find_common_section(map1, map2))

if __name__ == '__main__':
    main()

