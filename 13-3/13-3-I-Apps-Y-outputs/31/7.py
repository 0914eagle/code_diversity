
def get_optimized_path(path):
    # Initialize variables
    optimized_path = path
    endpoint = path[-1]
    min_substring_length = len(path)
    start_index, end_index = 0, 0

    # Iterate through the path
    for i in range(len(path)):
        # Check if the substring starting from index i is a valid substring
        if path[i] == endpoint:
            # If the substring is valid, check if it is the shortest possible
            if i - start_index + 1 < min_substring_length:
                # If it is the shortest possible, update the variables
                min_substring_length = i - start_index + 1
                start_index = i
                end_index = start_index + min_substring_length - 1

    # If a valid substring was found, return it
    if min_substring_length < len(path):
        return optimized_path[:start_index] + optimized_path[end_index+1:]
    # Otherwise, return -1
    else:
        return -1

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        path = input()
        optimized_path = get_optimized_path(path)
        if optimized_path == -1:
            print(-1)
        else:
            print(optimized_path)

if __name__ == '__main__':
    main()

