
def get_common_divisors(A, B):
    common_divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common_divisors.append(i)
    return common_divisors

def get_coprime_divisors(common_divisors):
    coprime_divisors = []
    for i in range(len(common_divisors)):
        for j in range(i+1, len(common_divisors)):
            if common_divisors[i] * common_divisors[j] == 1:
                coprime_divisors.append(common_divisors[i])
                coprime_divisors.append(common_divisors[j])
    return coprime_divisors

def get_max_divisors(A, B):
    common_divisors = get_common_divisors(A, B)
    coprime_divisors = get_coprime_divisors(common_divisors)
    return len(coprime_divisors)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(get_max_divisors(A, B))

