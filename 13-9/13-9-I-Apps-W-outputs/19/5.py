
def can_divide_array(a):
    n = len(a)
    sum1 = sum(a[:n//2])
    sum2 = sum(a[n//2:])
    if sum1 == sum2:
        return "YES"
    else:
        for i in range(n):
            for j in range(n):
                if i != j and a[i] + a[j] == sum1:
                    return "YES"
        return "NO"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(can_divide_array(a))

if __name__ == '__main__':
    main()

