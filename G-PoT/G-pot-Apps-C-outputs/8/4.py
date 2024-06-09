
n = int(input())

def is_power_of_two(x):
    return x != 0 and (x & (x - 1)) == 0

if n == 1 or is_power_of_two(n):
    print("Vasya")
else:
    print("Petya")
