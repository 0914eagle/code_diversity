
def get_party_array(n, photographs):
    # Initialize an array to store the party of each MP
    party = [' '] * (n + 1)
    
    # Iterate over the photographs
    for photograph in photographs:
        # Split the photograph into pairs of MPs scowling at each other
        pairs = photograph.split()
        
        # Iterate over the pairs
        for pair in pairs:
            # Split the pair into the two MPs
            mp1, mp2 = pair.split(',')
            
            # Check if both MPs have not been assigned a party yet
            if party[mp1] == ' ' and party[mp2] == ' ':
                # Assign them different parties
                party[mp1] = 'A'
                party[mp2] = 'B'
            # Check if only one MP has been assigned a party
            elif party[mp1] == ' ' or party[mp2] == ' ':
                # Assign the unassigned MP the opposite party
                if party[mp1] == ' ':
                    party[mp1] = 'B' if party[mp2] == 'A' else 'A'
                else:
                    party[mp2] = 'B' if party[mp1] == 'A' else 'A'
    
    # Return the party array
    return party

def main():
    n = int(input())
    photographs = []
    for _ in range(5):
        photographs.append(input())
    print(''.join(get_party_array(n, photographs)))

if __name__ == '__main__':
    main()

