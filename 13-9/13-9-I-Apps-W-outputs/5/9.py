
def read_input():
    n, k = map(int, input().split())
    lamps = []
    for _ in range(n):
        l, r = map(int, input().split())
        lamps.append((l, r))
    return n, k, lamps

def solve(n, k, lamps):
    # Initialize the answer
    answer = 0
    
    # Iterate over all possible combinations of k lamps
    for combination in itertools.combinations(lamps, k):
        # Check if the combination meets the condition
        if all(l <= r for l, r in combination):
            answer += 1
    
    # Return the answer modulo 998244353
    return answer % 998244353

def main():
    n, k, lamps = read_input()
    print(solve(n, k, lamps))

if __name__ == '__main__':
    main()

