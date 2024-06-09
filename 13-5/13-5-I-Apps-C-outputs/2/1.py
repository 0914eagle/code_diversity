
def f1(N, a, b):
    # Calculate the sum of the values of the candies for each sibling
    sum_a = sum(a)
    sum_b = sum(b)
    
    # Initialize the output string
    output = ""
    
    # Loop through each candy and assign it to the sibling with the highest value
    for i in range(N):
        if a[i] >= b[i]:
            output += "A"
        else:
            output += "B"
    
    # Return the output string
    return output

def f2(N, a, b):
    # Calculate the sum of the values of the candies for each sibling
    sum_a = sum(a)
    sum_b = sum(b)
    
    # Initialize the output string
    output = ""
    
    # Loop through each candy and assign it to the sibling with the highest value
    for i in range(N):
        if a[i] > b[i]:
            output += "A"
        elif a[i] < b[i]:
            output += "B"
        else:
            output += "A" if sum_a > sum_b else "B"
    
    # Return the output string
    return output

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(N, a, b))
    print(f2(N, a, b))

