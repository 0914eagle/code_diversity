
def get_min_paths(k_arr):
    # Initialize a dictionary to store the shortest path from each node to the assembly node
    min_paths = {}
    for i in range(len(k_arr)):
        min_paths[i] = float('inf')
    min_paths[0] = 0

    # Iterate through the nodes and update the shortest path from each node to the assembly node
    for i in range(len(k_arr)):
        for j in range(len(k_arr)):
            if k_arr[i] % k_arr[j] == 0 and min_paths[j] + 1 < min_paths[i]:
                min_paths[i] = min_paths[j] + 1

    # Return the sum of the shortest paths from each fragment to the assembly node
    return sum(min_paths.values())

def main():
    n = int(input())
    k_arr = list(map(int, input().split()))
    print(get_min_paths(k_arr))

if __name__ == '__main__':
    main()

