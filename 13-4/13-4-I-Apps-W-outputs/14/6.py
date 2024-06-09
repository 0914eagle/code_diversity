
def read_input():
    m, n = map(int, input().split())
    pictures = []
    for _ in range(m):
        pictures.append(list(map(int, input().split())))
    return m, n, pictures

def solve(m, n, pictures):
    # Initialize the time when each picture is ready for sale
    ready_time = [0] * m
    
    # Loop through each picture
    for i in range(m):
        # Loop through each painter
        for j in range(n):
            # Add the time it takes for the painter to paint the picture
            ready_time[i] += pictures[i][j]
    
    return ready_time

def print_output(ready_time):
    for i in ready_time:
        print(i, end=" ")
    print()

if __name__ == '__main__':
    m, n, pictures = read_input()
    ready_time = solve(m, n, pictures)
    print_output(ready_time)

