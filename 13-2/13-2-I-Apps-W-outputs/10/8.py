
def get_min_sets(nums):
    # Sort the numbers in descending order
    nums.sort(reverse=True)
    # Initialize the minimum number of sets to 0
    min_sets = 0
    # Loop through the numbers and check if they can be divided into sets
    for i, num in enumerate(nums):
        # If the current number is not divisible by the previous number, we need to add a new set
        if i > 0 and num % nums[i-1] != 0:
            min_sets += 1
    return min_sets

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(get_min_sets(nums))

if __name__ == '__main__':
    main()

