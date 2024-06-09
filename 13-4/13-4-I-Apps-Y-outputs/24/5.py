
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
            a.append(str(i))
    return a

def sum_fizzbuzz(n):
    a = fizzbuzz(n)
    s = 0
    for i in a:
        if i.isdigit():
            s += int(i)
    return s

if __name__ == '__main__':
    n = int(input())
    print(sum_fizzbuzz(n))

