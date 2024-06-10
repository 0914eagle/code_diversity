
def get_party(n, photographs):
    # Initialize an array to store the party of each MP
    party = [""] * (n + 1)
    
    # Loop through each photograph
    for photograph in photographs:
        # Split the photograph into pairs of MPs
        pairs = photograph.split()
        
        # Loop through each pair
        for pair in pairs:
            # Get the indices of the MPs
            i, j = map(int, pair.split(" "))
            
            # If both MPs have not been assigned a party yet
            if not party[i] and not party[j]:
                # Assign them to different parties
                party[i] = "A"
                party[j] = "B"
            # If only one MP has been assigned a party yet
            elif not party[i] or not party[j]:
                # Assign the unassigned MP to the other party
                party[i] = "B" if party[j] == "A" else "A"
    
    return "".join(party[1:])

def main():
    n = int(input())
    photographs = []
    for _ in range(5):
        photographs.append(input())
    print(get_party(n, photographs))

if __name__ == '__main__':
    main()

