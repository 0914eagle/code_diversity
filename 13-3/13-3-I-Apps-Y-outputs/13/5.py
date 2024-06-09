
A, P = map(int, input().split())

max_pies = 0

# We can make at most A/2 apple pies by simmering two pieces of apple
max_pies += A // 2

# If A is odd, we can make one more apple pie by simmering the remaining piece
if A % 2 == 1:
    max_pies += 1

# We can make at most P/3 apple pies by cutting the whole apple into three pieces and simmering two pieces
max_pies += P // 3

print(max_pies)

