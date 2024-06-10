
def get_common_factors(num1, num2):
    common_factors = []
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
            if num1 // i != i and num2 // i != i:
                common_factors.append(num1 // i)
                common_factors.append(num2 // i)
    return common_factors

def count_streamers(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if get_common_factors(nums[i], nums[j]):
                count += 1
    return count

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(count_streamers(nums) % 1000000007)

if __name__ == '__main__':
    main()

