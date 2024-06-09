
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of reposted pictures in the current segment
        beauty = sum(a[i:i+k])
        # Check if the current segment has at least one picture reposted by Vova
        if beauty > 0:
            # Update the maximum sum of values of reposted pictures
            max_beauty = max(max_beauty, beauty)
    
    # Check if the number of reposted pictures is less than or equal to x
    if max_beauty * k <= x:
        return max_beauty
    else:
        return -1

