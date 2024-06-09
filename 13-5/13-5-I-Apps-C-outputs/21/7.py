
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the pack sizes and their real amounts
    pack_sizes = {}
    for company in companies:
        for pack_size, real_amount in company:
            pack_sizes[pack_size] = real_amount

    # Initialize the smallest pack size as the bolts needed
    smallest_pack_size = bolts_needed

    # Iterate through the pack sizes and find the smallest pack that contains at least the bolts needed
    for pack_size, real_amount in pack_sizes.items():
        if real_amount >= bolts_needed:
            smallest_pack_size = min(smallest_pack_size, pack_size)

    return smallest_pack_size

def main():
    bolts_needed = int(input())
    companies = int(input())
    companies_info = []
    for _ in range(companies):
        company_info = input().split()
        companies_info.append([int(x) for x in company_info])
    smallest_pack_size = get_smallest_pack(bolts_needed, companies_info)
    print(smallest_pack_size)

if __name__ == '__main__':
    main()

