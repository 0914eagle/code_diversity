
def get_subsequence(a, b):
    # Initialize variables
    subsequence = []
    visited = set()
    
    # Iterate through the elements of a
    for element in a:
        # If the element is not in the visited set, add it to the subsequence
        if element not in visited:
            subsequence.append(element)
            visited.add(element)
    
    # Check if the subsequence is also a subsequence of b
    if all(element in subsequence for element in b):
        return subsequence
    else:
        return None

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        # Get the subsequence of a and b
        subsequence = get_subsequence(a, b)
        
        # Check if a subsequence exists
        if subsequence:
            print("YES")
            print(len(subsequence))
            print(*subsequence)
        else:
            print("NO")

if __name__ == '__main__':
    main()

