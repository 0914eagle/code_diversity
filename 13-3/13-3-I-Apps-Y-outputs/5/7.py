
def f1(r, c):
    # Initialize a 2D array to store the number of islands
    num_islands = [[0 for _ in range(c)] for _ in range(r)]

    # Loop through each row and column
    for i in range(r):
        for j in range(c):
            # If the current cell is land and it has not been visited yet, visit it and count the number of islands
            if image[i][j] == 'L' and num_islands[i][j] == 0:
                count_islands(i, j, num_islands)

    # Return the total number of islands
    return sum(sum(num_islands))

def count_islands(i, j, num_islands):
    # If the current cell is out of bounds or not land, return
    if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != 'L' or num_islands[i][j] != 0:
        return

    # Mark the current cell as visited
    num_islands[i][j] = 1

    # Recursively visit the neighboring cells
    count_islands(i-1, j, num_islands)
    count_islands(i+1, j, num_islands)
    count_islands(i, j-1, num_islands)
    count_islands(i, j+1, num_islands)

if __name__ == '__main__':
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    print(f1(r, c))

