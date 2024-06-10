
def calculate_sum(n):
    # Calculate the sum of all integers from 1 to n
    sum = (n * (n + 1)) // 2
    
    # Calculate the sum of all powers of two from 1 to n
    powers_of_two_sum = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0:
            powers_of_two_sum += i
    
    # Return the difference between the two sums
    return sum - powers_of_two_sum

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(calculate_sum(n))

if __name__ == '__main__':
    main()

