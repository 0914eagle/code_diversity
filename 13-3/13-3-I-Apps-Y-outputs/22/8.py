
def f1(N, A, x):
    # Calculate the sum of the integers written on the cards
    sum_x = sum(x)

    # Calculate the average of the integers written on the cards
    avg_x = sum_x / N

    # Calculate the number of ways to select cards such that the average is exactly A
    num_ways = 0
    for i in range(N):
        if x[i] == A:
            num_ways += 1
        elif x[i] + (N-1) * (A-avg_x) == sum_x:
            num_ways += 1

    return num_ways

def f2(...):
    ...

if __name__ == '__main__':
    N = int(input())
    A = int(input())
    x = list(map(int, input().split()))
    print(f1(N, A, x))

