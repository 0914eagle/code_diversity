
def get_coating_t(s, t):
    # Initialize variables
    n = 0
    pieces = []
    coating = ""
    
    # Loop through the shop coating
    for i in range(len(s)):
        # Check if the current piece is a prefix of the desired coating
        if s[i:i+len(t)] == t:
            # If it is, add it to the pieces list
            pieces.append((i, i+len(t)-1))
            # Update the coating
            coating += t
            # Break the loop
            break
        # Check if the current piece is a suffix of the desired coating
        if s[0:i+1] == t[len(t)-i-1:]:
            # If it is, add it to the pieces list
            pieces.append((0, i))
            # Update the coating
            coating = t[0:i+1] + coating
            # Break the loop
            break
    
    # If the coating is not empty, return the pieces list
    if coating:
        return pieces
    # If the coating is empty, return -1
    else:
        return -1

def get_coating_s(s, t):
    # Initialize variables
    n = 0
    pieces = []
    coating = ""
    
    # Loop through the shop coating
    for i in range(len(s)):
        # Check if the current piece is a prefix of the desired coating
        if s[i:i+len(t)] == t:
            # If it is, add it to the pieces list
            pieces.append((i, i+len(t)-1))
            # Update the coating
            coating += t
            # Break the loop
            break
        # Check if the current piece is a suffix of the desired coating
        if s[0:i+1] == t[len(t)-i-1:]:
            # If it is, add it to the pieces list
            pieces.append((0, i))
            # Update the coating
            coating = t[0:i+1] + coating
            # Break the loop
            break
    
    # If the coating is not empty, return the pieces list
    if coating:
        return pieces
    # If the coating is empty, return -1
    else:
        return -1

if __name__ == '__main__':
    s = input()
    t = input()
    print(get_coating_t(s, t))
    print(get_coating_s(s, t))

