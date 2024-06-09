
def is_power_of_two(n):
    return n & (n - 1) == 0

def find_highest_power_of_two(n):
    power = 0
    while n > 1:
        n //= 2
        power += 1
    return power

n = int(input())

if is_power_of_two(n):
    print("Petya")
else:
    highest_power = find_highest_power_of_two(n)
    if n % 2 == 0:
        print("Vasya")
    else:
        if highest_power % 2 == 0:
            print("Vasya")
        else:
            print("Petya")
