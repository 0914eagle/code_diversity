
def solve(a):
    # find the sum of all elements in the array
    sum_a = sum(a)
    
    # if the sum is even, return the length of the array and the indices of all elements
    if sum_a % 2 == 0:
        return len(a), [i for i in range(len(a))]
    
    # if the sum is odd, return -1
    return -1
    
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
        
if __name__ == '__main__':
    main()

