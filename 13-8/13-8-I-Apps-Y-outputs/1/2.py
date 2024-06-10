
def read_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return r, c, image

def find_islands(image):
    # Initialize a 2D array to keep track of visited cells
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    # Initialize a queue to store the cells to be processed
    queue = []
    
    # Initialize a counter for the number of islands found
    num_islands = 0
    
    # Iterate over each cell in the image
    for i in range(r):
        for j in range(c):
            # If the current cell is not visited and it is land, mark it as visited and add it to the queue
            if not visited[i][j] and image[i][j] == 'L':
                visited[i][j] = True
                queue.append((i, j))
                
                # Perform BFS to find all the connected cells
                while queue:
                    i, j = queue.pop(0)
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < r and 0 <= y < c and not visited[x][y] and image[x][y] == 'L':
                            visited[x][y] = True
                            queue.append((x, y))
                            
                num_islands += 1
    
    return num_islands

def main():
    r, c, image = read_input()
    print(find_islands(image))

if __name__ == '__main__':
    main()

