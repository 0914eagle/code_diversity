
def get_smallest_pack(bolts, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts = {}
    for company in companies:
        min_bolts[company] = float('inf')

    # Initialize a dictionary to store the number of bolts in each pack from each company
    pack_bolts = {}
    for company in companies:
        pack_bolts[company] = {}

    # Loop through each company and calculate the minimum number of bolts required to buy a pack from that company
    for company in companies:
        for pack_size in companies[company]:
            min_bolts[company] = min(min_bolts[company], pack_size)

    # Loop through each company and calculate the number of bolts in each pack from that company
    for company in companies:
        for pack_size in companies[company]:
            pack_bolts[company][pack_size] = pack_size

    # Loop through each company and calculate the number of bolts in each pack from that company, considering the packs from the previous company
    for i in range(1, len(companies)):
        for company in companies[i:]:
            for pack_size in companies[company]:
                pack_bolts[company][pack_size] = pack_bolts[company][pack_size] + pack_bolts[i-1][pack_size]

    # Find the smallest pack that contains at least the required number of bolts
    for company in companies:
        for pack_size in companies[company]:
            if pack_bolts[company][pack_size] >= bolts:
                return pack_size

    return "impossible"

