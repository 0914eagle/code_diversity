
def get_steps(a, b):
    steps = []
    for i in range(1, a+b+1):
        if i % 2 == 0:
            steps.append("even")
        else:
            steps.append("odd")
    return steps

def check_interval(steps, l, r):
    even_steps = 0
    odd_steps = 0
    for i in range(l-1, r):
        if steps[i] == "even":
            even_steps += 1
        else:
            odd_steps += 1
    if even_steps == a and odd_steps == b:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    a, b = map(int, input().split())
    steps = get_steps(a, b)
    l, r = map(int, input().split())
    print(check_interval(steps, l, r))

