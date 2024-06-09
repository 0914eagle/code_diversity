
def get_input():
    N = int(input())
    stones = input()
    return N, stones

def is_disaster(stones):
    for i in range(len(stones) - 1):
        if stones[i] == 'W' and stones[i + 1] == 'R':
            return True
    return False

def swap_stones(stones, i, j):
    stones[i], stones[j] = stones[j], stones[i]
    return stones

def change_color(stones, i):
    if stones[i] == 'R':
        stones[i] = 'W'
    else:
        stones[i] = 'R'
    return stones

def solve(N, stones):
    operations = 0
    while is_disaster(stones):
        for i in range(N - 1):
            if stones[i] == 'W' and stones[i + 1] == 'R':
                stones = swap_stones(stones, i, i + 1)
                operations += 1
                break
        else:
            for i in range(N):
                if stones[i] == 'W':
                    stones = change_color(stones, i)
                    operations += 1
                    break
    return operations

if __name__ == '__main__':
    N, stones = get_input()
    print(solve(N, stones))

