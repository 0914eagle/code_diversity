
def count_bishwocks(pawns_string1, pawns_string2):
    # Initialize a list to store the positions of pawns
    pawns = []
    
    # Loop through the strings and append the positions of pawns to the list
    for i in range(len(pawns_string1)):
        if pawns_string1[i] == "X":
            pawns.append((i, 0))
        if pawns_string2[i] == "X":
            pawns.append((i, 1))
    
    # Initialize a set to store the positions of bishwocks
    bishwocks = set()
    
    # Loop through the list of pawns and check if any of them are in the same row or column as any of the bishwocks
    for pawn in pawns:
        for bishwock in bishwocks:
            if pawn[0] == bishwock[0] or pawn[1] == bishwock[1]:
                return len(bishwocks)
        
        # If the pawn is not in the same row or column as any of the bishwocks, add it to the set of bishwocks
        bishwocks.add(pawn)
    
    # If no pawns are in the same row or column as any of the bishwocks, return the number of bishwocks
    return len(bishwocks)

