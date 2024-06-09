
def get_remainder(n, x, y, num):
    # Convert the number to a list of digits
    num_list = [int(i) for i in str(num)]
    
    # Initialize the minimum number of operations to perform
    min_ops = 0
    
    # Iterate over the digits of the number
    for i in range(n):
        # If the current digit is 0 and the next digit is 1, flip the current digit
        if num_list[i] == 0 and i < n-1 and num_list[i+1] == 1:
            num_list[i] = 1
            min_ops += 1
    
    # If the number of operations is not evenly divisible by x, flip the last digit
    if min_ops % x != 0:
        num_list[-1] = 1 - num_list[-1]
        min_ops += 1
    
    # Return the minimum number of operations
    return min_ops

def main():
    n, x, y = map(int, input().split())
    num = int(input())
    print(get_remainder(n, x, y, num))

if __name__ == '__main__':
    main()

