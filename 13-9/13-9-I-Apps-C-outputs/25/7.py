
def get_input():
    n, m = map(int, input().split())
    nums = [int(input()) for _ in range(n)]
    return n, m, nums

def lossy_sort(nums, m):
    sorted_nums = sorted(nums)
    changes = 0
    for i in range(len(nums)):
        if sorted_nums[i] != nums[i]:
            changes += 1
            nums[i] = sorted_nums[i]
    return changes

def solve(n, m, nums):
    min_changes = float('inf')
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                changes = lossy_sort(nums, m)
                if changes < min_changes:
                    min_changes = changes
                    sorted_nums = nums[:]
    return sorted_nums

if __name__ == '__main__':
    n, m, nums = get_input()
    print(*solve(n, m, nums))

