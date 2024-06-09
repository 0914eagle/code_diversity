
def solve(n, v, sellers):
    # Find the sellers who have items with a price less than or equal to v
    possible_sellers = []
    for seller in sellers:
        for item in seller:
            if item <= v:
                possible_sellers.append(seller)
                break
    
    # Return the number of possible sellers and their indices
    return len(possible_sellers), [sellers.index(seller) for seller in possible_sellers]

