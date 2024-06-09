
def f1(C, K):
    # Calculate the nearest amount that Mirko can pay
    nearest_amount = int(C / (10 ** K)) * (10 ** K)
    if C % (10 ** K) >= (10 ** K) / 2:
        nearest_amount += (10 ** K)
    return nearest_amount

def f2(C, K):
    # Calculate the nearest amount that Mirko can pay using a loop
    nearest_amount = 0
    for i in range(K):
        nearest_amount += (10 ** i) * (C // (10 ** i))
        C %= (10 ** i)
    return nearest_amount

if __name__ == '__main__':
    C, K = map(int, input().split())
    print(f1(C, K))
    print(f2(C, K))

