
def f1(n, a):
    # Calculate the sum of all angles
    sum_angles = sum(a)
    
    # Initialize the minimum difference between angles
    min_diff = sum_angles
    
    # Iterate over all possible combinations of pieces
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the sum of angles for Vasya's sector
            vasya_sum = sum(a[:i+1])
            
            # Calculate the sum of angles for Petya's sector
            petya_sum = sum(a[i+1:j+1])
            
            # Calculate the difference between the two sectors
            diff = abs(vasya_sum - petya_sum)
            
            # Update the minimum difference
            min_diff = min(min_diff, diff)
    
    return min_diff

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

