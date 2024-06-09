
def get_common_divisors(a):
    common_divisors = set(a)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            common_divisors.intersection_update(range(min(a[i], a[j]), max(a[i], a[j])+1, abs(a[i]-a[j])))
    return len(common_divisors)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_common_divisors(a))

if __name__ == '__main__':
    main()

