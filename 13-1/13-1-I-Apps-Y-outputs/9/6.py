
def f1(a, b, c):
    return sorted([a, b, c])

def f2(a, b, c):
    return [a, c, b]

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    desired_order = input()
    if desired_order == 'ABC':
        print(*f1(a, b, c))
    else:
        print(*f2(a, b, c))

