
def is_winning_strategy(n, k, c):
    # Check if k is in the list of ancient numbers
    if k in c:
        return "Yes"
    
    # Check if any two ancient numbers have a common remainder
    for i in range(n):
        for j in range(i+1, n):
            if c[i] % k == c[j] % k:
                return "No"
    
    # If the program reaches this point, then Arya has a winning strategy
    return "Yes"

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    print(is_winning_strategy(n, k, c))

if __name__ == '__main__':
    main()

