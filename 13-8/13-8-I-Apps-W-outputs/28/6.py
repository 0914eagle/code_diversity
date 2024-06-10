
def get_even_odd_steps(a, b):
    even_steps = []
    odd_steps = []
    for i in range(1, a+1):
        even_steps.append(i*2)
    for i in range(1, b+1):
        odd_steps.append(i*2-1)
    return even_steps, odd_steps

def check_interval(l, r, even_steps, odd_steps):
    count_even = 0
    count_odd = 0
    for i in range(l, r+1):
        if i in even_steps:
            count_even += 1
        if i in odd_steps:
            count_odd += 1
    if count_even == count_odd:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    a, b = map(int, input().split())
    even_steps, odd_steps = get_even_odd_steps(a, b)
    l, r = map(int, input().split())
    print(check_interval(l, r, even_steps, odd_steps))

