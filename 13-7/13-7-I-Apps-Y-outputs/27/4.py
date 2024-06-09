
def get_max_sum_of_reposted_pictures(n, k, x, a):
    # Calculate the maximum sum of values of reposted pictures
    max_sum = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of reposted pictures
        sum_of_beauty = sum(a[i:i+k])
        # Check if the sum of beauty values is greater than the current maximum sum
        if sum_of_beauty > max_sum:
            max_sum = sum_of_beauty
    
    # Check if the number of reposted pictures is less than x
    if max_sum < x:
        return -1
    else:
        return max_sum

