
def get_largest_xor_sum(n, k):
    candies = list(range(1, n+1))
    return max(xor_sum(candies[i:i+k]) for i in range(n-k+1))

def xor_sum(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

