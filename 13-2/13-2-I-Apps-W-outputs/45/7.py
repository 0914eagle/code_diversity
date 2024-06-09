
def can_rejoin_necklace(necklace):
    # Initialize variables
    num_links = 0
    num_pearls = 0
    adjacent_pearls = []

    # Iterate through the necklace
    for i in range(len(necklace)):
        if necklace[i] == '-':
            num_links += 1
        elif necklace[i] == 'o':
            num_pearls += 1
            if i > 0 and necklace[i-1] == 'o':
                adjacent_pearls.append(necklace[i-1])
            if i < len(necklace)-1 and necklace[i+1] == 'o':
                adjacent_pearls.append(necklace[i+1])

    # Check if the number of links between adjacent pearls is equal
    for pearl in adjacent_pearls:
        if adjacent_pearls.count(pearl) != num_links:
            return "NO"

    return "YES"

if __name__ == '__main__':
    necklace = input()
    print(can_rejoin_necklace(necklace))

