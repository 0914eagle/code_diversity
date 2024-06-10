
def get_boring_pairs(n, paths):
    # Initialize a dictionary to store the number of boring pairs for each step
    boring_pairs = {0: 0}

    # Iterate through the paths and increment the number of boring pairs for each step
    for path in paths:
        step = path[2]
        boring_pairs[step] = boring_pairs.get(step, 0) + 1

    # Return the number of boring pairs for each step
    return boring_pairs

def main():
    # Read the input
    n = int(input())
    paths = []
    for _ in range(n - 1):
        paths.append(list(map(int, input().split())))
    order = list(map(int, input().split()))

    # Get the number of boring pairs for each step
    boring_pairs = get_boring_pairs(n, paths)

    # Print the number of boring pairs after each step
    for i in range(1, n):
        print(boring_pairs[i])

if __name__ == '__main__':
    main()

