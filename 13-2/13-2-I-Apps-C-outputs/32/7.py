
def get_smallest_pack(bolts, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts = {}
    for company in companies:
        min_bolts[company] = float('inf')

    # Initialize a dictionary to store the number of bolts in each pack from each company
    pack_bolts = {}
    for company in companies:
        pack_bolts[company] = {}

    # Loop through the companies and calculate the minimum number of bolts required to buy a pack from each company
    for company in companies:
        for pack in companies[company]:
            min_bolts[company] = min(min_bolts[company], pack)
            pack_bolts[company][pack] = pack

    # Loop through the companies and calculate the number of bolts in each pack from each company
    for company in companies:
        for pack in companies[company]:
            if pack >= min_bolts[company]:
                pack_bolts[company][pack] = pack
            else:
                pack_bolts[company][pack] = min_bolts[company]

    # Find the smallest pack that contains at least the required number of bolts
    smallest_pack = float('inf')
    for company in companies:
        for pack in pack_bolts[company]:
            if pack >= bolts and pack < smallest_pack:
                smallest_pack = pack

    # If a pack is found, return its size, otherwise return 'impossible'
    if smallest_pack != float('inf'):
        return smallest_pack
    else:
        return 'impossible'

def main():
    bolts = int(input())
    companies = int(input())
    companies_info = {}
    for i in range(companies):
        company, *pack_sizes = input().split()
        companies_info[company] = [int(pack_size) for pack_size in pack_sizes]
    print(get_smallest_pack(bolts, companies_info))

if __name__ == '__main__':
    main()

