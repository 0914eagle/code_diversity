
def get_smallest_pack_size(bolts_needed, companies):
    # Initialize a dictionary to store the pack sizes and their real amounts
    pack_sizes = {}
    for company in companies:
        for pack_size, real_amount in company:
            pack_sizes[pack_size] = real_amount

    # Initialize the smallest pack size as impossible
    smallest_pack_size = "impossible"

    # Iterate through the pack sizes in descending order
    for pack_size in sorted(pack_sizes.keys(), reverse=True):
        # If the pack size is greater than or equal to the bolts needed, return the pack size
        if pack_size >= bolts_needed:
            smallest_pack_size = pack_size
            break

    return smallest_pack_size

def main():
    # Read the bolts needed and the number of companies from stdin
    bolts_needed, num_companies = map(int, input().split())

    # Read the pack sizes and real amounts for each company from stdin
    companies = []
    for _ in range(num_companies):
        company = []
        for _ in range(int(input())):
            pack_size, real_amount = map(int, input().split())
            company.append((pack_size, real_amount))
        companies.append(company)

    # Call the function to get the smallest pack size
    smallest_pack_size = get_smallest_pack_size(bolts_needed, companies)

    # Print the smallest pack size
    print(smallest_pack_size)

if __name__ == '__main__':
    main()

