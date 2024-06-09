
def get_optimized_path(path):
    # Initialize variables
    optimized_path = path
    endpoint = path[-1]
    min_substring_length = len(path)
    substring_start, substring_end = 0, 0

    # Iterate over all possible substrings
    for i in range(len(path)):
        for j in range(i+1, len(path)+1):
            # Check if the substring is non-empty and ends at the endpoint
            if j-i > 1 and path[j-1] == endpoint:
                # Check if the substring length is less than the current minimum
                if j-i < min_substring_length:
                    # Update the minimum substring length and endpoints
                    min_substring_length = j-i
                    substring_start = i
                    substring_end = j-1

    # Return the optimized path and endpoints
    return optimized_path[:substring_start] + optimized_path[substring_end+1:], substring_start, substring_end

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate over the test cases
    for _ in range(num_test_cases):
        # Read the path length and path
        path_length = int(input())
        path = input()

        # Get the optimized path and endpoints
        optimized_path, start, end = get_optimized_path(path)

        # Check if the optimized path is empty
        if optimized_path == "":
            # Print -1 if the optimized path is empty
            print(-1)
        else:
            # Print the optimized path and endpoints
            print(optimized_path, start, end)

if __name__ == '__main__':
    main()

