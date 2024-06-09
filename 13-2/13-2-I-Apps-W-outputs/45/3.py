
def can_rejoin_necklace(necklace):
    # Initialize variables
    num_links = necklace.count('-')
    num_pearls = necklace.count('o')
    num_adjacent_pearls = num_pearls - 1
    num_links_between_pearls = num_links // num_adjacent_pearls
    
    # Check if the number of links between adjacent pearls is equal
    if num_links_between_pearls * num_adjacent_pearls == num_links:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    necklace = input()
    print(can_rejoin_necklace(necklace))

