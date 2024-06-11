def minSubArraySum(nums):
    
    # init
    min_sum = float('inf')
    cur_sum = 0
    # loop
    for num in nums:
        cur_sum += num
        min_sum = min(min_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return min_sum


if __name__ == '__main__':
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))
    print(minSubArraySum([-1, -2, -3]))
