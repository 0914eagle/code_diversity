
def get_input():
    return list(map(int, input().split()))

def is_multiple_of_a(n, a):
    return n % a == 0

def is_congruent_to_c_modulo_b(sum_of_selected_numbers, c, b):
    return sum_of_selected_numbers % b == c

def select_numbers(a, b, c):
    selected_numbers = []
    current_sum = 0
    while current_sum < c:
        current_sum += a
        selected_numbers.append(current_sum)
    return selected_numbers

def main():
    a, b, c = get_input()
    selected_numbers = select_numbers(a, b, c)
    if is_multiple_of_a(selected_numbers[0], a) and is_congruent_to_c_modulo_b(sum(selected_numbers), c, b):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

