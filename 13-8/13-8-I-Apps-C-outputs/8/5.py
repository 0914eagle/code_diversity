
def get_longest_exploration_sequence(array, d, m):
    # Initialize a dictionary to store the longest exploration sequence for each element
    longest_sequence = {element: 1 for element in array}

    # Loop through the array and calculate the longest exploration sequence for each element
    for i in range(len(array)):
        for j in range(i+1, min(i+d+1, len(array))):
            if abs(array[i] - array[j]) <= m:
                longest_sequence[array[j]] = max(longest_sequence[array[j]], longest_sequence[array[i]] + 1)

    # Return the longest exploration sequence for the last element in the array
    return longest_sequence[array[-1]]

def main():
    n, d, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(get_longest_exploration_sequence(array, d, m))

if __name__ == '__main__':
    main()

