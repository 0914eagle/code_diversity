
def solve(n, k, a):
    # Step 1: Sort the array in non-decreasing order
    a.sort()
    
    # Step 2: Initialize the minimum number of moves to 0
    min_moves = 0
    
    # Step 3: Loop through the array and find the minimum and maximum values
    min_value = a[0]
    max_value = a[n-1]
    
    # Step 4: Loop through the array and check if there are at least k equal elements
    for i in range(n):
        if a[i] == min_value:
            min_moves += 1
        if a[i] == max_value:
            min_moves -= 1
    
    # Step 5: Return the minimum number of moves
    return min_moves

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))

if __name__ == '__main__':
    main()

