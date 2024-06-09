
def solve(N):
    sum = 0
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            sum += "FizzBuzz"
        elif i % 3 == 0:
            sum += "Fizz"
        elif i % 5 == 0:
            sum += "Buzz"
        else:
            sum += str(i)
    return sum

