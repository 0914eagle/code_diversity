
def f1(s):
    # Function to calculate the average value of L(C) for a given sequence S
    # Initialize variables
    n = len(s)
    count = 0
    sum = 0
    
    # Iterate over all possible sequences C represented by S
    for i in range(1, n+1):
        for j in range(n-i+1):
            # Calculate the number of operations before Prof. Tuy stops for the current sequence C
            k = i
            while k <= n and s[k-1] == 'H':
                k += 1
            if k <= n:
                count += 1
                sum += k
    
    # Calculate the average value of L(C)
    return sum / count

def f2(s):
    # Function to solve the problem for a given sequence S
    # Initialize variables
    n = len(s)
    count = 0
    sum = 0
    
    # Iterate over all possible sequences C represented by S
    for i in range(1, n+1):
        for j in range(n-i+1):
            # Calculate the number of operations before Prof. Tuy stops for the current sequence C
            k = i
            while k <= n and s[k-1] == 'H':
                k += 1
            if k <= n:
                count += 1
                sum += k
    
    # Calculate the average value of L(C)
    avg = sum / count
    
    # Print the output
    print(avg)

if __name__ == '__main__':
    s = input()
    f2(s)

