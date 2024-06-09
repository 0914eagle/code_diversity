
def solve(numbers):
    n = len(numbers)
    if n == 1:
        return "YES"
    if n == 2:
        if numbers[0] < numbers[1]:
            return "YES"
        else:
            return "NO"
    if n == 3:
        if numbers[0] < numbers[1] + numbers[2] and numbers[1] < numbers[2] + numbers[0] and numbers[2] < numbers[0] + numbers[1]:
            return "YES"
        else:
            return "NO"
    else:
        for i in range(n):
            sum1 = numbers[i] + numbers[(i+1)%n]
            sum2 = numbers[i] + numbers[(i-1)%n]
            if sum1 < numbers[(i+1)%n] or sum2 < numbers[(i-1)%n]:
                return "NO"
        return "YES"

