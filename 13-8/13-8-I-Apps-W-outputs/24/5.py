
def get_d_magic_numbers(m, d, a, b):
    count = 0
    for i in range(a, b+1):
        if i % m == 0 and str(i).count(str(d)) > 0:
            count += 1
    return count

def get_answer(m, d, a, b):
    count = get_d_magic_numbers(m, d, a, b)
    return count % (10**9 + 7)

if __name__ == '__main__':
    m, d = map(int, input().split())
    a, b = map(int, input().split())
    print(get_answer(m, d, a, b))

