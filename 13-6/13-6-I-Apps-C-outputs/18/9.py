
def is_perfect_square(n):
    return int(n**0.5)**2 == n

def largest_not_perfect_square(arr):
    return max([x for x in arr if not is_perfect_square(x)])

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(largest_not_perfect_square(arr))

