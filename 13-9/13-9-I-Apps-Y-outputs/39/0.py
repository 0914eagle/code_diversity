
def is_possible(a, b, c):
    # Initialize a list to store the selected integers
    selected_integers = []
    
    # Loop through all multiples of a starting from a
    for i in range(a, b+1, a):
        # If the sum of the selected integers plus the current integer is congruent to c modulo b, add the current integer to the list
        if (sum(selected_integers) + i) % b == c:
            selected_integers.append(i)
    
    # If the list is not empty, return YES, otherwise return NO
    if selected_integers:
        return "YES"
    else:
        return "NO"

def main():
    # Read a, b, and c from stdin
    a, b, c = map(int, input().split())
    
    # Call the is_possible function and print the result
    print(is_possible(a, b, c))

if __name__ == '__main__':
    main()

