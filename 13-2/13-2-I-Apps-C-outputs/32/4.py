
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack from each company
    min_bolts_required = {}
    for company in companies:
        min_bolts_required[company] = float('inf')

    # Initialize a dictionary to store the number of bolts in each pack from each company
    num_bolts_in_pack = {}
    for company in companies:
        num_bolts_in_pack[company] = {}

    # Loop through each company and calculate the minimum number of bolts required to buy a pack from that company
    for company in companies:
        for pack_size in companies[company]:
            if pack_size >= bolts_needed:
                min_bolts_required[company] = min(min_bolts_required[company], pack_size)
                num_bolts_in_pack[company][pack_size] = pack_size
            else:
                break

    # Loop through each company and calculate the number of bolts in each pack from that company
    for company in companies:
        for pack_size in companies[company]:
            if pack_size >= bolts_needed:
                num_bolts_in_pack[company][pack_size] = pack_size
            else:
                break

    # Find the smallest pack size that is greater than or equal to the number of bolts needed
    smallest_pack_size = float('inf')
    for company in companies:
        for pack_size in companies[company]:
            if pack_size >= bolts_needed and pack_size < smallest_pack_size:
                smallest_pack_size = pack_size
                break

    # If a pack size was found, return it, otherwise return "impossible"
    if smallest_pack_size != float('inf'):
        return smallest_pack_size
    else:
        return "impossible"

def main():
    bolts_needed = int(input())
    num_companies = int(input())
    companies = {}
    for i in range(num_companies):
        company_info = input().split()
        company = company_info[0]
        num_pack_sizes = int(company_info[1])
        pack_sizes = []
        for j in range(2, num_pack_sizes+2):
            pack_sizes.append(int(company_info[j]))
        companies[company] = pack_sizes
    print(get_smallest_pack(bolts_needed, companies))

if __name__ == '__main__':
    main()

