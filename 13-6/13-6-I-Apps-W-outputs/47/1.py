
def find_subset(a):
    # Find the sum of all elements in the array
    sum_of_elements = sum(a)
    
    # If the sum is even, return the length of the array and the indexes of all elements
    if sum_of_elements % 2 == 0:
        return len(a), [i for i in range(1, len(a) + 1)]
    
    # If the sum is odd, return -1
    return -1

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the length of the array
        n = int(input())
        
        # Read the array
        a = list(map(int, input().split()))
        
        # Find the subset
        result = find_subset(a)
        
        # Print the result
        if result == -1:
            print(-1)
        else:
            print(result[0])
            print(" ".join(map(str, result[1])))

if __name__ == '__main__':
    main()

