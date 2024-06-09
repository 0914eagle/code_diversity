
def get_gcd(numbers):
    return functools.reduce(lambda a, b: a * b // math.gcd(a, b), numbers)

def get_min_subset_size(numbers):
    gcd = get_gcd(numbers)
    if gcd == 1:
        return len(numbers)
    
    for i in range(len(numbers)):
        if numbers[i] % gcd == 0:
            return i
    
    return -1

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_min_subset_size(numbers))

if __name__ == '__main__':
    main()

