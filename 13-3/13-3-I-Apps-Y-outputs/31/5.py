
def get_optimized_path(path):
    # Initialize variables
    optimized_path = path
    endpoint = path[-1]
    min_substring_length = len(path)
    start_index, end_index = 0, 0

    # Iterate over all possible substrings
    for i in range(len(path)):
        for j in range(i+1, len(path)+1):
            # Check if the substring is non-empty and ends at the endpoint
            if j-i > 1 and path[j-1] == endpoint:
                # Check if the substring length is less than the current minimum
                if j-i < min_substring_length:
                    # Update the minimum substring length and indices
                    min_substring_length = j-i
                    start_index = i
                    end_index = j-1

    # Return the optimized path
    return optimized_path[:start_index] + optimized_path[end_index+1:]

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate over the test cases
    for _ in range(num_test_cases):
        # Read the path length and the path
        path_length = int(input())
        path = input()

        # Get the optimized path
        optimized_path = get_optimized_path(path)

        # Check if the optimized path is empty
        if len(optimized_path) == 0:
            print(-1)
        else:
            # Print the start and end indices of the substring to remove
            print(1, len(path))

if __name__ == '__main__':
    main()

