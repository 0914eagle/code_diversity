
def get_even_odd_numbers(n):
    even = 0
    odd = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def check_interval(l, r, a, b):
    even, odd = get_even_odd_numbers(r)
    return a <= even and b <= odd and even - a == odd - b

def main():
    l, r = map(int, input().split())
    a, b = map(int, input().split())
    print("YES" if check_interval(l, r, a, b) else "NO")

if __name__ == '__main__':
    main()

