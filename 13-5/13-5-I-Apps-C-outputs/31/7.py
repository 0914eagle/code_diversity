
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the number of bolts in each pack
    packs = {}

    # Loop through each company
    for company in companies:
        # Loop through each pack size offered by the company
        for pack_size in company:
            # If the pack size is not already in the dictionary, add it
            if pack_size not in packs:
                packs[pack_size] = 0
            # Increment the number of bolts in the pack
            packs[pack_size] += pack_size

    # Loop through the dictionary of packs and find the smallest pack that contains at least the number of bolts needed
    for pack_size, num_bolts in packs.items():
        if num_bolts >= bolts_needed:
            return pack_size

    # If no pack contains at least the number of bolts needed, return "impossible"
    return "impossible"

