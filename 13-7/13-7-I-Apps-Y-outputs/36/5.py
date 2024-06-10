
def get_longest_increasing_sequence(a):
    # Initialize variables
    n = len(a)
    left = [0] * n
    right = [0] * n
    longest = 0
    longest_index = -1
    
    # Compute the length of the longest increasing subsequence
    # that ends at index i and starts at the left
    for i in range(n):
        left[i] = 1 + left[i-1] if i > 0 and a[i] > a[i-1] else 1
        if left[i] > longest:
            longest = left[i]
            longest_index = i
    
    # Compute the length of the longest increasing subsequence
    # that ends at index i and starts at the right
    for i in range(n-1, -1, -1):
        right[i] = 1 + right[i+1] if i < n-1 and a[i] > a[i+1] else 1
        if right[i] > longest:
            longest = right[i]
            longest_index = i
    
    # Find the longest increasing subsequence that starts at the left
    # and ends at the right
    left_index = 0
    right_index = n-1
    while left_index < longest_index:
        if left[left_index] < right[right_index]:
            left_index += 1
        else:
            right_index -= 1
    
    # Construct the longest increasing subsequence
    sequence = []
    while left_index <= right_index:
        sequence.append(a[left_index])
        left_index += 1
        right_index -= 1
    
    return sequence

def solve(a):
    sequence = get_longest_increasing_sequence(a)
    return len(sequence), ''.join('L' if a[i] == sequence[0] else 'R' for i in range(len(a)))

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(solve(a))

