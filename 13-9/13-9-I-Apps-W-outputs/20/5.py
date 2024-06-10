
def k_rounding(n, k):
    # Convert n to a string
    n_str = str(n)
    
    # Initialize a variable to store the rounded number
    rounded_num = 0
    
    # Iterate through the digits of n_str
    for i in range(len(n_str)):
        # If the current digit is not a 0, break the loop
        if n_str[i] != '0':
            break
        # If the current digit is a 0 and the number of zeros is greater than or equal to k, add a 0 to the rounded number
        elif i >= k:
            rounded_num += 1
    
    # Return the rounded number
    return rounded_num

def main():
    # Input the values of n and k
    n, k = map(int, input().split())
    
    # Call the k_rounding function and print the result
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

