
def get_common_factors(num1, num2):
    common_factors = []
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
            if num1 // i != i and num2 // i != i:
                common_factors.append(num1 // i)
                common_factors.append(num2 // i)
    return common_factors

def get_num_ways(nums):
    num_ways = 1
    for i in range(len(nums)):
        common_factors = get_common_factors(nums[i], nums[(i+1)%len(nums)])
        num_ways *= len(common_factors)
    return num_ways % (10**9 + 7)

if __name__ == '__main__':
    num_students = int(input())
    nums = []
    for _ in range(num_students):
        nums.append(int(input()))
    print(get_num_ways(nums))

