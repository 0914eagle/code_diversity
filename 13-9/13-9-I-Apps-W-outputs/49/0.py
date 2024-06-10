
def get_max_presents(n, s, a):
    # Find the sum of the times it takes to recite each part of the verse
    sum_a = sum(a)
    
    # If the sum of the times is less than or equal to the maximum number of seconds Santa will listen to Vasya, then Vasya can recite the whole verse and get the maximum number of gifts
    if sum_a <= s:
        return 0
    
    # Initialize the maximum number of gifts to be obtained
    max_gifts = 0
    
    # Initialize the part to be skipped to obtain the maximum number of gifts
    skip_part = 0
    
    # Iterate over each part of the verse
    for i in range(n):
        # Calculate the number of gifts Vasya will get if he skips the current part
        gifts = s // a[i]
        
        # If the number of gifts is greater than the current maximum, update the maximum and the part to be skipped
        if gifts > max_gifts:
            max_gifts = gifts
            skip_part = i
    
    # Return the part to be skipped to obtain the maximum number of gifts
    return skip_part

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_max_presents(n, s, a))

if __name__ == '__main__':
    main()

