
def get_steps_with_even_and_odd_numbers(a, b):
    steps = []
    for i in range(1, int(a / 2) + 1):
        steps.append(2 * i)
    for i in range(1, int((b - a) / 2) + 1):
        steps.append(2 * i + 1)
    return steps

def check_interval(l, r, a, b):
    steps = get_steps_with_even_and_odd_numbers(a, b)
    for i in range(l - 1, r):
        if steps[i] % 2 == 0 and steps[i] != 2 * (i + 1):
            return "NO"
        if steps[i] % 2 == 1 and steps[i] != 2 * (i + 1) + 1:
            return "NO"
    return "YES"

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(check_interval(1, 100, a, b))

