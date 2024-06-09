
def count_winning_moves(N, numbers):
    count = 0
    for i in range(N):
        if numbers[i] % 2 != 0:
            count += 1
    return min(count, N - count)

N = int(input())
numbers = list(map(int, input().split()))

print(count_winning_moves(N, numbers))
