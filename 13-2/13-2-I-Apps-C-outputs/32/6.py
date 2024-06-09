
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts_required = {}
    for company in companies:
        min_bolts_required[company] = float('inf')

    # Initialize a dictionary to store the number of bolts in each pack from each company
    num_bolts_in_pack = {}
    for company in companies:
        num_bolts_in_pack[company] = {}

    # Loop through each company and its pack sizes
    for company, pack_sizes in companies.items():
        for pack_size in pack_sizes:
            # If the pack size is less than or equal to the number of bolts needed, update the minimum number of bolts required to buy a pack from this company
            if pack_size <= bolts_needed:
                min_bolts_required[company] = min(min_bolts_required[company], pack_size)
            # If the pack size is greater than the number of bolts needed, update the number of bolts in the pack from this company
            if pack_size > bolts_needed:
                num_bolts_in_pack[company][pack_size] = pack_size

    # Loop through each company and its pack sizes again
    for company, pack_sizes in companies.items():
        for pack_size in pack_sizes:
            # If the pack size is greater than the minimum number of bolts required to buy a pack from this company, update the number of bolts in the pack from this company
            if pack_size > min_bolts_required[company]:
                num_bolts_in_pack[company][pack_size] = pack_size - min_bolts_required[company]

    # Find the smallest pack size that contains at least the number of bolts needed
    smallest_pack_size = float('inf')
    for company, pack_sizes in num_bolts_in_pack.items():
        for pack_size, num_bolts in pack_sizes.items():
            if num_bolts >= bolts_needed and pack_size < smallest_pack_size:
                smallest_pack_size = pack_size

    # If a pack size was found, return it, otherwise return 'impossible'
    if smallest_pack_size != float('inf'):
        return smallest_pack_size
    else:
        return 'impossible'

if __name__ == '__main__':
    bolts_needed = int(input())
    companies = int(input())
    companies_info = {}
    for i in range(companies):
        company, num_pack_sizes = input().split()
        num_pack_sizes = int(num_pack_sizes)
        pack_sizes = []
        for j in range(num_pack_sizes):
            pack_size = int(input())
            pack_sizes.append(pack_size)
        companies_info[company] = pack_sizes
    print(get_smallest_pack(bolts_needed, companies_info))

