
def fizzbuzz(n):
    a = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            a.append("FizzBuzz")
        elif i % 3 == 0:
            a.append("Fizz")
        elif i % 5 == 0:
            a.append("Buzz")
        else:
            a.append(i)
    return a

def sum_fizzbuzz(n):
    a = fizzbuzz(n)
    sum = 0
    for i in a:
        if type(i) == int:
            sum += i
    return sum

if __name__ == '__main__':
    n = int(input())
    print(sum_fizzbuzz(n))

