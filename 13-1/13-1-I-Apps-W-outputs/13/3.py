
import sys

def get_subsets(nums):
    subsets = []
    for i in range(1 << len(nums)):
        subset = []
        for j in range(len(nums)):
            if i & (1 << j):
                subset.append(nums[j])
        subsets.append(subset)
    return subsets

def get_sum(subset, nums):
    return sum(nums[i] for i in subset)

def get_f(subset, nums, s):
    return 1 if get_sum(subset, nums) == s else 0

def solve(nums, s):
    subsets = get_subsets(nums)
    return sum(get_f(subset, nums, s) for subset in subsets) % 998244353

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    s = int(input())
    print(solve(nums, s))

