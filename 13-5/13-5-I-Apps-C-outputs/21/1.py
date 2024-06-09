
def get_smallest_pack_size(bolts_needed, companies):
    # Initialize a list to store the smallest pack size that contains at least the number of bolts needed
    smallest_pack_sizes = []

    # Loop through each company
    for company in companies:
        # Loop through each pack size offered by the company
        for pack_size in company:
            # If the pack size is greater than or equal to the number of bolts needed, add it to the list of smallest pack sizes
            if pack_size >= bolts_needed:
                smallest_pack_sizes.append(pack_size)

    # If the list of smallest pack sizes is empty, return "impossible"
    if not smallest_pack_sizes:
        return "impossible"

    # Otherwise, return the smallest pack size in the list
    return min(smallest_pack_sizes)

def main():
    # Read the number of bolts needed and the number of companies from stdin
    bolts_needed, num_companies = map(int, input().split())

    # Read the pack sizes offered by each company from stdin
    companies = []
    for _ in range(num_companies):
        companies.append(list(map(int, input().split())))

    # Call the get_smallest_pack_size function and print the result
    print(get_smallest_pack_size(bolts_needed, companies))

if __name__ == '__main__':
    main()

