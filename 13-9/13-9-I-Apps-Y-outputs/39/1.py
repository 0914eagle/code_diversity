
def get_input():
    return list(map(int, input().split()))

def is_multiple_of_a(n, a):
    return n % a == 0

def calculate_sum(numbers):
    return sum(numbers)

def is_sum_congruent_to_c_modulo_b(numbers, a, b, c):
    sum_ = calculate_sum(numbers)
    return sum_ % b == c

def main():
    a, b, c = get_input()
    numbers = []
    while True:
        n = int(input())
        if n == 0:
            break
        if is_multiple_of_a(n, a):
            numbers.append(n)
    if len(numbers) == 0:
        print("NO")
    elif is_sum_congruent_to_c_modulo_b(numbers, a, b, c):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

