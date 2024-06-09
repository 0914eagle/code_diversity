
def get_arithmetic_progression(n, a):
    # Calculate the difference between consecutive terms
    diff = a[1] - a[0]
    # Check if the sequence is already an arithmetic progression
    if all(a[i+1] - a[i] == diff for i in range(n-1)):
        return [-1]
    
    # Find the missing term in the sequence
    missing_term = a[0] + (n-1) * diff
    return [missing_term]

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def main():
    n, a = get_input()
    result = get_arithmetic_progression(n, a)
    print(len(result))
    print(*result)

if __name__ == '__main__':
    main()

