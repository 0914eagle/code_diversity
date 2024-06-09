
def get_least_number_of_digits_1(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def get_addends(n):
    addends = []
    while n > 0:
        addends.append(n % 10)
        n = n // 10
    return addends

def get_least_number_of_digits_1_in_sum(n):
    addends = get_addends(n)
    count = 0
    for addend in addends:
        count += get_least_number_of_digits_1(addend)
    return count

if __name__ == '__main__':
    n = int(input())
    print(get_least_number_of_digits_1_in_sum(n))

