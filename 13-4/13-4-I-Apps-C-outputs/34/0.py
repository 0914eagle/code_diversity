
def get_powers_of_2(n):
    powers_of_2 = []
    for i in range(63):
        powers_of_2.append(2**i)
    return powers_of_2

def count_powers_of_2(n, e):
    powers_of_2 = get_powers_of_2(n)
    count = 0
    for i in range(n+1):
        if str(i) in [str(p) for p in powers_of_2 if p <= n]:
            count += 1
    return count

if __name__ == '__main__':
    n, e = map(int, input().split())
    print(count_powers_of_2(n, e))

