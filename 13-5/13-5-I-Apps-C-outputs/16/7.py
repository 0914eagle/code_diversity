
def is_solvable(n, k, rows):
    # Initialize a set to store the numbers that are already filled in
    filled_nums = set()
    for row in rows:
        for num in row:
            filled_nums.add(num)
    # Check if all numbers from 1 to n are filled in
    for num in range(1, n + 1):
        if num not in filled_nums:
            return False
    return True

def solve_superdoku(n, k, rows):
    # Initialize a set to store the numbers that are already filled in
    filled_nums = set()
    for row in rows:
        for num in row:
            filled_nums.add(num)
    # Check if all numbers from 1 to n are filled in
    for num in range(1, n + 1):
        if num not in filled_nums:
            return False
    return True

def main():
    n, k = map(int, input().split())
    rows = [list(map(int, input().split())) for _ in range(k)]
    if is_solvable(n, k, rows):
        print("yes")
        print(*solve_superdoku(n, k, rows))
    else:
        print("no")

if __name__ == '__main__':
    main()

