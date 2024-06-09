
def solve(n, k):
    # Initialize a dictionary to store the frequency of each letter
    freq = {}
    for i in range(1, k+1):
        freq[i] = 0
    
    # Initialize a list to store the letters of the string
    s = []
    
    # Loop through each letter of the string
    for i in range(n):
        # Find the letter with the minimum frequency
        min_freq = min(freq.values())
        min_key = [k for k, v in freq.items() if v == min_freq][0]
        
        # Update the frequency of the letter
        freq[min_key] += 1
        
        # Add the letter to the string
        s.append(chr(min_key + 96))
    
    return "".join(s)

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

if __name__ == '__main__':
    main()

