
def solve():
    N = int(input())
    T = input()
    
    # Initialize a counter for the number of occurrences
    count = 0
    
    # Loop through the concatenation of 3 copies of 110
    for i in range(3*N):
        # Check if the substring T occurs at the current position
        if T == "110"[i%3]:
            count += 1
    
    # Print the number of occurrences
    print(count)

