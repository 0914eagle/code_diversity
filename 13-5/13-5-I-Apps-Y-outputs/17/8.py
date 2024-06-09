
def get_min_mp(l_list, a, b, c):
    # Sort the list of lengths in non-decreasing order
    l_list.sort()
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0
    # Initialize the current length of the bamboos
    current_length = 0
    # Loop through the list of lengths
    for l in l_list:
        # If the current length is less than the required length, use the extension magic
        if current_length < a:
            min_mp += 1
            current_length += 1
        # If the current length is greater than the required length, use the shortening magic
        elif current_length > a:
            min_mp += 1
            current_length -= 1
        # If the current length is equal to the required length, use the composition magic
        else:
            min_mp += 10
            current_length = l + current_length
    # Return the minimum MP needed to achieve the objective
    return min_mp

def get_input():
    # Get the number of bamboos and the required lengths
    n, a, b, c = map(int, input().split())
    # Get the list of lengths
    l_list = list(map(int, input().split()))
    # Return the number of bamboos, the required lengths, and the list of lengths
    return n, a, b, c, l_list

if __name__ == '__main__':
    # Get the input
    n, a, b, c, l_list = get_input()
    # Calculate the minimum MP needed to achieve the objective
    min_mp = get_min_mp(l_list, a, b, c)
    # Print the minimum MP needed to achieve the objective
    print(min_mp)

