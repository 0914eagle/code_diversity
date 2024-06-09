
def get_power_of_two(n):
    power = 1
    while power <= n:
        power *= 2
    return power

def get_numbers_with_power_of_two(n, e):
    power_of_two = get_power_of_two(e)
    count = 0
    for i in range(n):
        if str(i).find(str(power_of_two)) != -1:
            count += 1
    return count

def main():
    n, e = map(int, input().split())
    print(get_numbers_with_power_of_two(n, e))

if __name__ == '__main__':
    main()

