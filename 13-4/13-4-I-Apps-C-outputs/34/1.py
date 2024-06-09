
def get_powers_of_two(n):
    powers_of_two = []
    for i in range(63):
        powers_of_two.append(2**i)
    return powers_of_two

def count_powers_of_two(n, e):
    powers_of_two = get_powers_of_two(n)
    count = 0
    for i in range(n+1):
        if str(i) in [str(p) for p in powers_of_two if p <= n]:
            count += 1
    return count

if __name__ == '__main__':
    n, e = map(int, input().split())
    print(count_powers_of_two(n, e))

