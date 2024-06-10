
def get_d_magic_numbers(m, d, a, b):
    d_magic_numbers = []
    for i in range(a, b+1):
        if i % m == 0 and str(i)[::2].count(str(d)) > 0:
            d_magic_numbers.append(i)
    return d_magic_numbers

def get_remainder(d_magic_numbers):
    return sum(d_magic_numbers) % (10**9 + 7)

if __name__ == '__main__':
    m, d = map(int, input().split())
    a, b = map(int, input().split())
    d_magic_numbers = get_d_magic_numbers(m, d, a, b)
    print(get_remainder(d_magic_numbers))

