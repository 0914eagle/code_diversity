
def is_perfect_square(n):
    return int(n**0.5)**2 == n

def find_largest_non_perfect_square(arr):
    non_perfect_squares = []
    for num in arr:
        if not is_perfect_square(num):
            non_perfect_squares.append(num)
    return max(non_perfect_squares)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_largest_non_perfect_square(arr))

if __name__ == '__main__':
    main()

