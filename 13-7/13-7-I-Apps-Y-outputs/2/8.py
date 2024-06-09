
def solve(n):
    # Initialize a set to store the numbers that can be obtained from n
    nums = set()
    # Add n to the set
    nums.add(n)
    # Initialize a variable to store the minimum number of moves required to obtain 1 from n
    min_moves = 0
    # Loop until the set contains 1
    while 1 not in nums:
        # If the set is empty, it means it is impossible to obtain 1 from n, so return -1
        if not nums:
            return -1
        # Initialize a variable to store the next number in the set
        next_num = 0
        # Loop through the numbers in the set
        for num in nums:
            # If the number is divisible by 2, add its half to the set
            if num % 2 == 0:
                nums.add(num // 2)
            # If the number is divisible by 3, add its double divided by 3 to the set
            if num % 3 == 0:
                nums.add(num * 2 // 3)
            # If the number is divisible by 5, add its double divided by 5 to the set
            if num % 5 == 0:
                nums.add(num * 4 // 5)
            # If the next number has not been initialized, initialize it to the current number
            if not next_num:
                next_num = num
        # Add the next number to the set
        nums.add(next_num)
        # Increment the minimum number of moves required to obtain 1 from n
        min_moves += 1
    # Return the minimum number of moves required to obtain 1 from n
    return min_moves

