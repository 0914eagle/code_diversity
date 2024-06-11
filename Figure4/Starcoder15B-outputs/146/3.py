def specialFilter(nums):
    
    return len([num for num in nums if (num > 10 and isOdd(num) and isOdd(lastDigit(num)))])

