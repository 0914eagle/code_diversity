
def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    return n, numbers

def get_first_moves(n, numbers):
    first_moves = set()
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] % 2 == 1:
                first_moves.add(i)
                first_moves.add(j)
    return len(first_moves)

def main():
    n, numbers = get_input()
    print(get_first_moves(n, numbers))

if __name__ == '__main__':
    main()

