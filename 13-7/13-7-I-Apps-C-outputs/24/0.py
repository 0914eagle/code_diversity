
def get_input():
    N = int(input())
    numbers = list(map(int, input().split()))
    return N, numbers

def get_first_moves(N, numbers):
    first_moves = set()
    for i in range(N):
        for j in range(i+1, N):
            if numbers[i] + numbers[j] % 2 == 1:
                first_moves.add(numbers[i])
                first_moves.add(numbers[j])
    return first_moves

def main():
    N, numbers = get_input()
    first_moves = get_first_moves(N, numbers)
    print(len(first_moves))

if __name__ == '__main__':
    main()

