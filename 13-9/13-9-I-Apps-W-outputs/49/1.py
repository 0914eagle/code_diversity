
def solve(n, s, a):
    # Find the sum of the times it takes to recite each part of the verse
    sum_a = sum(a)
    
    # If the sum of the times is less than or equal to the maximum number of seconds Santa will listen to Vasya, then Vasya can recite the whole verse and get the maximum number of gifts
    if sum_a <= s:
        return 0
    
    # Initialize the maximum number of gifts Vasya can get by skipping a part of the verse
    max_gifts = 0
    
    # Initialize the part of the verse that Vasya needs to skip to get the maximum number of gifts
    skip_part = 0
    
    # Iterate over each part of the verse
    for i in range(n):
        # If Vasya skips the current part of the verse
        if a[i] <= s:
            # Calculate the number of gifts Vasya can get by skipping the current part of the verse
            gifts = sum(a[i+1:])
            
            # If the number of gifts is greater than the maximum number of gifts Vasya can get by skipping a part of the verse
            if gifts > max_gifts:
                # Update the maximum number of gifts Vasya can get by skipping a part of the verse
                max_gifts = gifts
                
                # Update the part of the verse that Vasya needs to skip to get the maximum number of gifts
                skip_part = i
    
    # Return the part of the verse that Vasya needs to skip to get the maximum number of gifts
    return skip_part

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, s, a))

if __name__ == '__main__':
    main()

