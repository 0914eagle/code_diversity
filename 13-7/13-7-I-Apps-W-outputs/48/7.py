
def get_maximum_bourles(n, m, r, s, b):
    # Initialize variables
    max_bourles = r
    shares = 0
    i = 0
    j = 0
    
    # Loop through the opportunities to buy and sell shares
    while i < n and j < m:
        # If the current buy opportunity is cheaper than the current sell opportunity, buy as many shares as possible
        if s[i] <= b[j]:
            shares += (r - b[j]) // s[i]
            r = (r - b[j]) % s[i]
            i += 1
        # If the current sell opportunity is cheaper than the current buy opportunity, sell as many shares as possible
        else:
            max_bourles = max(max_bourles, r + shares * b[j])
            j += 1
    
    # If there are still opportunities left, buy as many shares as possible with the remaining bourles
    while i < n:
        shares += r // s[i]
        r = r % s[i]
        i += 1
    
    # Return the maximum number of bourles after the evening
    return max(max_bourles, r + shares * b[-1])

def main():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_maximum_bourles(n, m, r, s, b))

if __name__ == '__main__':
    main()

