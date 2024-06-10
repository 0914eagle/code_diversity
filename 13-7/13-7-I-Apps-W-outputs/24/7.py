
def calculate_sum(n):
    # Calculate the sum of all integers from 1 to n
    sum = (n * (n + 1)) // 2
    
    # Subtract the powers of two from the sum
    for i in range(n.bit_length()):
        sum -= 2 ** i
    
    return sum

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for _ in range(t):
        # Read the input n
        n = int(input())
        
        # Calculate the sum
        sum = calculate_sum(n)
        
        # Print the result
        print(sum)

if __name__ == '__main__':
    main()

