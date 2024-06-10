
def get_even_odd_steps(a, b):
    even_steps = []
    odd_steps = []
    for i in range(1, a+1):
        even_steps.append(2*i)
    for i in range(1, b+1):
        odd_steps.append(2*i-1)
    return even_steps, odd_steps

def check_interval(l, r, even_steps, odd_steps):
    even_count = 0
    odd_count = 0
    for i in range(l, r+1):
        if i in even_steps:
            even_count += 1
        if i in odd_steps:
            odd_count += 1
    return even_count == odd_count

if __name__ == '__main__':
    a, b = map(int, input().split())
    even_steps, odd_steps = get_even_odd_steps(a, b)
    l, r = map(int, input().split())
    print("YES") if check_interval(l, r, even_steps, odd_steps) else print("NO")

