
def solve(n, s, a):
    # Find the maximum number of gifts Vasya can get by reciting the whole verse
    max_gifts = sum(a)
    
    # Initialize the minimum number of gifts Vasya can get by skipping one part
    min_gifts = 0
    
    # Iterate through each part of the verse
    for i in range(n):
        # Calculate the number of gifts Vasya can get by skipping the current part
        gifts = sum(a[j] for j in range(i)) + sum(a[j] for j in range(i + 1, n))
        
        # If the number of gifts is greater than the maximum number of gifts, update the maximum number of gifts
        if gifts > max_gifts:
            max_gifts = gifts
        
        # If the number of gifts is less than the minimum number of gifts, update the minimum number of gifts
        if gifts < min_gifts:
            min_gifts = gifts
    
    # Return the part number that Vasya needs to skip to obtain the maximum number of gifts
    return max_gifts - min_gifts

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, s, a))

if __name__ == '__main__':
    main()

