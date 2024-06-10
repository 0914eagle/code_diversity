
def is_integer_sold(A, B, X):
    # Find the largest integer that can be bought with X yen
    max_integer = (X - B) // A
    
    # Check if the largest integer is valid
    if max_integer >= 1:
        return max_integer
    else:
        return 0

def main():
    # Read input from stdin
    A, B, X = map(int, input().split())
    
    # Call the is_integer_sold function and print the result
    print(is_integer_sold(A, B, X))

if __name__ == '__main__':
    main()

