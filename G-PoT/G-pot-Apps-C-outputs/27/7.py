
def count_winning_moves(N, numbers):
    count = 0
    for i in range(N):
        if numbers[i] % 2 != 0:
            count += 1
    return count

# Read input
N = int(input())
numbers = list(map(int, input().split()))

# Find and output the number of winning moves
print(count_winning_moves(N, numbers))
