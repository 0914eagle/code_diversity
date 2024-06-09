
def get_min_operations(s, t):
    # Initialize variables
    min_operations = 0
    s_list = list(s)
    t_list = list(t)

    # Loop through both strings and check for differences
    for i in range(len(s)):
        if s_list[i] != t_list[i]:
            min_operations += 1
            s_list[i] = t_list[i]

    # Return the minimum number of operations required
    return min_operations

def main():
    # Read input from stdin
    s = input()
    t = input()

    # Call the get_min_operations function and print the result
    print(get_min_operations(s, t))

if __name__ == '__main__':
    main()

