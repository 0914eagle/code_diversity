
def get_power_of_two(n, e):
    power_of_two = 1
    for i in range(e):
        power_of_two *= 2
    return power_of_two

def count_numbers_with_power_of_two(n, e):
    power_of_two = get_power_of_two(n, e)
    count = 0
    for i in range(n):
        if str(i).find(str(power_of_two)) != -1:
            count += 1
    return count

if __name__ == '__main__':
    n, e = map(int, input().split())
    print(count_numbers_with_power_of_two(n, e))

