
def count_winning_moves(N, numbers):
    count = 0
    for i in range(N):
        if (numbers[i] % 2 != 0) or (numbers[(i+1) % N] % 2 != 0) or (numbers[(i-1) % N] % 2 != 0):
            count += 1
    return count

# Input
N = int(input())
numbers = list(map(int, input().split()))

# Output
print(count_winning_moves(N, numbers))
