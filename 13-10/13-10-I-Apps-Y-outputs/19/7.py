
def get_median_string(s, t):
    # Find the middle index of the list of strings
    mid_index = (len(s) - 1) // 2
    
    # Return the middle string
    return s[mid_index]

def main():
    # Read the input
    k = int(input())
    s = input()
    t = input()
    
    # Call the function to find the median string
    median = get_median_string(s, t)
    
    # Print the result
    print(median)

if __name__ == '__main__':
    main()

