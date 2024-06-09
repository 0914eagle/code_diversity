
def get_smallest_pack(bolts, companies):
    # Initialize a dictionary to store the minimum number of bolts required for each company
    min_bolts = {company: float('inf') for company in companies}
    # Initialize a dictionary to store the number of bolts in each pack
    pack_bolts = {}

    # Loop through each company and their packs
    for company, packs in companies.items():
        # Loop through each pack and its advertised number of bolts
        for pack, bolts in packs.items():
            # If the advertised number of bolts is less than the minimum required, skip this pack
            if bolts < min_bolts[company]:
                continue
            # If the pack contains more bolts than required, add it to the dictionary of packs
            if bolts >= bolts:
                pack_bolts[pack] = bolts

    # Find the smallest pack that contains at least the required number of bolts
    for pack, bolts in pack_bolts.items():
        if bolts >= bolts:
            return pack

    # If no pack contains the required number of bolts, return "impossible"
    return "impossible"

def main():
    bolts = int(input())
    companies = int(input())
    companies = {}
    for _ in range(companies):
        company, *packs = input().split()
        companies[company] = {int(pack): int(bolts) for pack, bolts in zip(packs[::2], packs[1::2])}
    print(get_smallest_pack(bolts, companies))

if __name__ == '__main__':
    main()

