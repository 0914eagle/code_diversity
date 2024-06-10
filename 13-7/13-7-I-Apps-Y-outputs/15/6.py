
def get_lexicographically_kth_string(n, k):
    # Initialize a list to store the strings
    strings = []
    
    # Iterate over all possible combinations of 'a' and 'b'
    for i in range(n):
        for j in range(n):
            if i + j == n - 2:
                # If the number of 'a' is equal to the number of 'b',
                # add the string to the list
                strings.append('a' * i + 'b' * j)
    
    # Sort the list lexicographically
    strings.sort()
    
    # Return the k-th string from the list
    return strings[k - 1]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(get_lexicographically_kth_string(n, k))

if __name__ == '__main__':
    main()

