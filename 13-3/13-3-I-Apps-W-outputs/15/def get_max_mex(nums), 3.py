
def get_max_mex(nums):
    # Convert the list to a set to remove duplicates
    nums = set(nums)
    # Initialize the maximum value of mex(A) + mex(B) as 0
    max_value = 0
    # Iterate over all possible subsets of the set
    for i in range(1 << len(nums)):
        # Convert the binary representation of i to a list of indices
        subset = [index for index in range(len(nums)) if i & (1 << index)]
        # Check if the subset is valid
        if len(subset) > 0 and len(subset) < len(nums):
            # Get the mex of the subset
            mex = get_mex(subset, nums)
            # Get the complement of the subset
            complement = list(nums - set(subset))
            # Get the mex of the complement
            mex_complement = get_mex(complement, nums)
            # Update the maximum value
            max_value = max(max_value, mex + mex_complement)
    return max_value

def get_mex(subset, nums):
    # Initialize the mex as 0
    mex = 0
    # Iterate over all numbers in the set
    for num in nums:
        # Check if the number is not in the subset
        if num not in subset:
            # Increment the mex
            mex += 1
    return mex

def solve(nums):
    return get_max_mex(nums)

