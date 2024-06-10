
def find_smallest_n(remembered_substring, n_digits):
    # Initialize a list to store all possible values of n
    n_list = []
    
    # Iterate through all possible values of n
    for i in range(10**(n_digits-1)):
        n = i * 10**n_digits
        n_str = str(n)
        if n_str.endswith(remembered_substring):
            n_list.append(n)
    
    # Return the smallest value of n
    return min(n_list)

def main():
    remembered_substring = input()
    n_digits = len(remembered_substring)
    print(find_smallest_n(remembered_substring, n_digits))

if __name__ == '__main__':
    main()

