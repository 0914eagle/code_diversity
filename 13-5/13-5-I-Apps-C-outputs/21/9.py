
def get_smallest_pack(bolts_needed, companies):
    # Initialize a dictionary to store the information about the companies and their packs
    company_packs = {}
    for company in companies:
        company_packs[company] = {}
        for pack in companies[company]:
            company_packs[company][pack] = companies[company][pack]
    
    # Initialize a list to store the smallest pack found so far
    smallest_pack = []
    
    # Iterate through the companies and their packs
    for company in company_packs:
        for pack in company_packs[company]:
            # Check if the pack contains at least the number of bolts needed
            if company_packs[company][pack] >= bolts_needed:
                # If the pack is smaller than the smallest pack found so far, update the smallest pack
                if len(smallest_pack) == 0 or len(smallest_pack) > len(pack):
                    smallest_pack = pack
    
    # Return the smallest pack found
    return smallest_pack

def main():
    # Read the input
    bolts_needed = int(input())
    companies = int(input())
    for i in range(companies):
        company, packs = input().split()
        companies[company] = {}
        for pack in packs.split(","):
            companies[company][pack] = int(pack)
    
    # Call the function to get the smallest pack
    smallest_pack = get_smallest_pack(bolts_needed, companies)
    
    # Print the output
    if len(smallest_pack) == 0:
        print("impossible")
    else:
        print(smallest_pack)

if __name__ == '__main__':
    main()

