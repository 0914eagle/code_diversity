
def get_maximum_gifts(n, s, a):
    # Find the sum of the times it takes to recite each part of the verse
    sum_a = sum(a)
    
    # If the sum of the times is less than or equal to the maximum number of seconds Santa will listen to Vasya, then Vasya can recite the whole verse and get the maximum number of gifts
    if sum_a <= s:
        return 0
    
    # Initialize the maximum number of gifts as 0
    max_gifts = 0
    
    # Initialize the part that Vasya needs to skip as 0
    skip_part = 0
    
    # Iterate over each part of the verse
    for i in range(n):
        # If Vasya skips the current part, then he gets the sum of the times it takes to recite all the parts except the current part
        gifts = sum_a - a[i]
        
        # If the number of gifts is greater than the maximum number of gifts, then update the maximum number of gifts and the part that Vasya needs to skip
        if gifts > max_gifts:
            max_gifts = gifts
            skip_part = i
    
    # Return the part that Vasya needs to skip to obtain the maximum number of gifts
    return skip_part

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_maximum_gifts(n, s, a))

if __name__ == '__main__':
    main()

