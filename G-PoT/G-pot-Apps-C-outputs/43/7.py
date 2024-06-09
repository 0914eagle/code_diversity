
def solve_dance(N, moves):
    result = [''] * N
    for i in range(N):
        if i % 2 == 0:
            result[i] = 'L'
        else:
            result[i] = 'R'

    for i in range(N):
        if result[i] == 'L':
            next_pos = (i + moves[i]) % N
        else:
            next_pos = (i - moves[i]) % N

        if result[next_pos] != '':
            return "no dance"

        result[next_pos] = result[i]

    return ''.join(result)

# Read input
N = int(input())
moves = list(map(int, input().split()))

# Call the function and print the output
print(solve_dance(N, moves))
