
def get_common_subsequence(a, b):
    # Find the length of the shortest array
    shortest_len = min(len(a), len(b))
    # Iterate over the shortest array
    for i in range(shortest_len):
        # Check if the current element of a is in b
        if a[i] in b:
            # If it is, return the current element and the rest of the array
            return [a[i]] + get_common_subsequence(a[i+1:], b)
    # If the current element is not in b, return an empty array
    return []

def get_smallest_common_subsequence(a, b):
    # Find the length of the shortest array
    shortest_len = min(len(a), len(b))
    # Initialize the smallest common subsequence with an empty array
    smallest_cs = []
    # Iterate over the shortest array
    for i in range(shortest_len):
        # Check if the current element of a is in b
        if a[i] in b:
            # If it is, find the common subsequence starting from this element
            current_cs = get_common_subsequence(a[i:], b)
            # If the current common subsequence is shorter than the smallest common subsequence found so far, update the smallest common subsequence
            if len(current_cs) < len(smallest_cs):
                smallest_cs = current_cs
    # Return the smallest common subsequence
    return smallest_cs

def main():
    # Read the number of test cases
    num_cases = int(input())
    # Iterate over the test cases
    for case in range(num_cases):
        # Read the lengths of the two arrays
        a_len, b_len = map(int, input().split())
        # Read the elements of the two arrays
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        # Find the smallest common subsequence
        smallest_cs = get_smallest_common_subsequence(a, b)
        # Check if a smallest common subsequence exists
        if smallest_cs:
            # If it does, print "YES" and the length and elements of the smallest common subsequence
            print("YES")
            print(len(smallest_cs))
            print(" ".join(map(str, smallest_cs)))
        else:
            # If it doesn't, print "NO"
            print("NO")

if __name__ == '__main__':
    main()

