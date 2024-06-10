
def get_num_supported_stewards(n, strengths):
    # Sort the strengths in ascending order
    strengths.sort()
    
    # Initialize variables to keep track of the number of stewards supported
    num_supported = 0
    i = 0
    j = n - 1
    
    # Iterate through the strengths and check if there is a steward with strength less than or greater than the current steward
    while i < j:
        if strengths[i] < strengths[j]:
            num_supported += 1
            i += 1
        elif strengths[i] > strengths[j]:
            num_supported += 1
            j -= 1
        else:
            num_supported += 2
            i += 1
            j -= 1
    
    # If there is only one steward, return 0
    if n == 1:
        return 0
    
    # Return the number of stewards supported
    return num_supported

def main():
    n = int(input())
    strengths = list(map(int, input().split()))
    print(get_num_supported_stewards(n, strengths))

if __name__ == '__main__':
    main()

