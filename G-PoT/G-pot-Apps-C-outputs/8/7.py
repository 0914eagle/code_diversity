
def is_power_of_two(x):
    return x & (x - 1) == 0

def find_highest_power_of_two(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)

def vasya_or_petya(n):
    if n == 1:
        return "Vasya"
    else:
        highest_power = find_highest_power_of_two(n)
        if n == highest_power:
            return "Petya"
        else:
            return "Vasya"

n = int(input())
print(vasya_or_petya(n))
