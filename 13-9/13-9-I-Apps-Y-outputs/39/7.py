
def find_solution(a, b, c):
    # Initialize a list to store the selected integers
    selected_integers = []
    
    # Iterate through the possible integers starting from a
    for i in range(a, b+1, a):
        # If the current integer is congruent to c modulo b, add it to the list
        if i % b == c:
            selected_integers.append(i)
    
    # If at least one integer is found, return YES, otherwise return NO
    if selected_integers:
        return "YES"
    else:
        return "NO"

def main():
    # Read a, b, and c from stdin
    a, b, c = map(int, input().split())
    
    # Call the find_solution function and print the result
    print(find_solution(a, b, c))

if __name__ == '__main__':
    main()

