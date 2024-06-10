
def get_solutions(A, B):
    # Initialize variables
    n = len(A)
    solutions = 0
    
    # Iterate through all possible groups of consecutive students
    for i in range(n):
        for j in range(i+1, n+1):
            # Check if the group of students has the same length as the input string
            if j - i == len(B):
                # Check if the group of students has the same characters as the input string
                if A[i:j] == B:
                    solutions += 1
    
    return solutions

def main():
    # Read input from stdin
    A = input()
    B = input()
    
    # Call the get_solutions function and print the result
    print(get_solutions(A, B))

if __name__ == '__main__':
    main()

