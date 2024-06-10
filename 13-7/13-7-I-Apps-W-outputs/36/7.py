
def get_common_subsequence(a, b):
    # Find the length of the shortest array
    shortest_len = min(len(a), len(b))
    # Iterate through the shortest array
    for i in range(shortest_len):
        # Check if the current element of a is in b
        if a[i] in b:
            # If it is, return the current element and the rest of the array
            return [a[i]] + get_common_subsequence(a[i+1:], b)
    # If the current element of a is not in b, return an empty array
    return []

def get_common_subsequences(a, b):
    # Initialize an empty list to store the common subsequences
    common_subsequences = []
    # Get the length of the shortest array
    shortest_len = min(len(a), len(b))
    # Iterate through the shortest array
    for i in range(shortest_len):
        # Check if the current element of a is in b
        if a[i] in b:
            # If it is, add the current element and the rest of the array to the list of common subsequences
            common_subsequences.append([a[i]] + get_common_subsequence(a[i+1:], b))
    # Return the list of common subsequences
    return common_subsequences

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    # Iterate through the test cases
    for i in range(num_test_cases):
        # Read the lengths of the two arrays and the arrays themselves
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        # Get the common subsequences of the two arrays
        common_subsequences = get_common_subsequences(a, b)
        # Check if any common subsequence exists
        if len(common_subsequences) > 0:
            # If it does, find the smallest possible length of a common subsequence
            smallest_length = min(map(len, common_subsequences))
            # Find the common subsequence with the smallest possible length
            smallest_common_subsequence = list(filter(lambda x: len(x) == smallest_length, common_subsequences))[0]
            # Print "YES" and the common subsequence
            print("YES")
            print(len(smallest_common_subsequence), *smallest_common_subsequence)
        else:
            # If no common subsequence exists, print "NO"
            print("NO")

if __name__ == '__main__':
    main()

