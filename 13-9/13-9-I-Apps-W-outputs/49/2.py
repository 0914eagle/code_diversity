
def get_maximum_gifts(a, s):
    # Find the sum of the time it takes to recite each part of the verse
    sum_of_parts = sum(a)
    
    # If the sum of the parts is less than or equal to the maximum number of seconds Santa will listen to Vasya, then Vasya can recite the whole verse and get the maximum number of gifts
    if sum_of_parts <= s:
        return 0
    
    # Initialize the maximum number of gifts to 0
    max_gifts = 0
    
    # Iterate over each part of the verse
    for i in range(len(a)):
        # If Vasya skips the current part, he will get the sum of the time it takes to recite all the previous parts
        gifts = sum(a[:i])
        
        # If the sum of the time it takes to recite all the previous parts is greater than or equal to the maximum number of seconds Santa will listen to Vasya, then Vasya can skip the current part and get the maximum number of gifts
        if gifts >= s:
            max_gifts = max(max_gifts, gifts)
    
    return max_gifts

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_maximum_gifts(a, s))

if __name__ == '__main__':
    main()

