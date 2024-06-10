
def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def count_subsequences(a, k):
    # Initialize a dictionary to store the count of each subsequence
    d = {}
    for i in range(n+1):
        d[i] = 0
    
    # Loop through each element in the sequence
    for i in range(n+1):
        # If the current element is not the last element in the sequence
        if i != n:
            # Loop through each possible next element
            for j in range(i+1, n+1):
                # If the current element and the next element are different
                if a[i] != a[j]:
                    # Increment the count of the subsequence with the current element and the next element
                    d[i] += 1
    
    # Return the count of the subsequence with the given length
    return d[k]

def main():
    n, a = read_input()
    for k in range(1, n+1):
        print(count_subsequences(a, k))

if __name__ == '__main__':
    main()

