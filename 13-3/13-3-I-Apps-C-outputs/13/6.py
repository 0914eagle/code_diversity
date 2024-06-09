
def get_common_remainders(numbers):
    remainders = set()
    for num in numbers:
        for i in range(1, num):
            if num % i == 0:
                remainders.add(i)
    return list(remainders)

