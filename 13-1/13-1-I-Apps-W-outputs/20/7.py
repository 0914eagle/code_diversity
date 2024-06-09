
def get_common_divisors(A, B):
    common_divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common_divisors.append(i)
    return common_divisors

def get_coprime_divisors(common_divisors):
    coprime_divisors = []
    for i in common_divisors:
        if all(i % j != 0 for j in coprime_divisors):
            coprime_divisors.append(i)
    return coprime_divisors

def get_maximum_divisors(A, B):
    common_divisors = get_common_divisors(A, B)
    coprime_divisors = get_coprime_divisors(common_divisors)
    return len(coprime_divisors)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(get_maximum_divisors(A, B))

