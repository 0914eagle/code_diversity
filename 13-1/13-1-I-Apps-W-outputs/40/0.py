
def f1(n, a):
    # Calculate the sum of all angles
    sum_angles = sum(a)
    
    # Initialize the minimum difference between angles
    min_diff = sum_angles
    
    # Iterate over all possible combinations of pieces
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the difference between the angles of the two sectors
            diff = abs(sum(a[i:j]) - sum(a[j:i]))
            
            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

