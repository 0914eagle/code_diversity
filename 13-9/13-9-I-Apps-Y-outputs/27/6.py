
def solve(n, f):
    # Initialize a dictionary to map each friend to their gift recipient
    gift_map = {}
    
    # Iterate through the input array
    for i in range(n):
        # If the current friend doesn't know who to give the gift to, set their gift recipient to the next friend in the array
        if f[i] == 0:
            gift_map[i] = (i + 1) % n
        # Otherwise, set their gift recipient to the friend specified in the input array
        else:
            gift_map[i] = f[i] - 1
    
    # Initialize an array to store the final output
    output = []
    
    # Iterate through the dictionary and add the gift recipients to the output array
    for i in range(n):
        output.append(gift_map[i] + 1)
    
    return output

