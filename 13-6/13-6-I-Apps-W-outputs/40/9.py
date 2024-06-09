
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def sum_of_divisors(n):
    divisors = get_divisors(n)
    return sum(divisors)

def sum_of_k_times_f(n):
    result = 0
    for k in range(1, n + 1):
        result += k * sum_of_divisors(k)
    return result

if __name__ == '__main__':
    n = int(input())
    print(sum_of_k_times_f(n))

