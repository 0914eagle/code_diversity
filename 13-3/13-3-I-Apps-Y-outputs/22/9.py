
def f1(N, A, x):
    # Calculate the sum of the integers on the cards
    sum_x = sum(x)

    # Calculate the number of ways to select cards such that the average is exactly A
    num_ways = 0
    for i in range(1, N+1):
        # Calculate the average of the selected cards
        avg = sum_x / i

        # Check if the average is exactly A
        if avg == A:
            num_ways += 1

    return num_ways

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N = int(input())
    A = int(input())
    x = list(map(int, input().split()))
    print(f1(N, A, x))

