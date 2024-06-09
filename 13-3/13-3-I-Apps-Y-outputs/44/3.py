
def f1(n, k):
    # Initialize a dictionary to store the frequency of each letter
    freq = {}
    for i in range(1, k+1):
        freq[chr(i+96)] = 0
    
    # Initialize a list to store the characters of the string
    s = []
    
    # Loop through each character of the string
    for i in range(n):
        # Find the letter with the minimum frequency
        min_freq = min(freq.values())
        min_key = [k for k, v in freq.items() if v == min_freq][0]
        
        # Add the letter to the string
        s.append(min_key)
        
        # Increment the frequency of the letter
        freq[min_key] += 1
    
    return "".join(s)

def f2(...):
    ...

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(f1(n, k))

