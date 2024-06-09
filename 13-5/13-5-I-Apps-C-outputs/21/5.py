
def get_smallest_pack(bolts_needed, companies):
    # Initialize the smallest pack as impossible
    smallest_pack = "impossible"
    
    # Iterate through the companies
    for company in companies:
        # Get the packs produced by the company
        packs = company["packs"]
        
        # Iterate through the packs
        for pack in packs:
            # Check if the pack contains at least the required number of bolts
            if pack["advertised_amount"] >= bolts_needed:
                # Check if the pack is smaller than the current smallest pack
                if smallest_pack == "impossible" or pack["advertised_amount"] < smallest_pack:
                    # Update the smallest pack
                    smallest_pack = pack["advertised_amount"]
    
    # Return the smallest pack
    return smallest_pack

def get_companies(input_data):
    # Initialize the companies list
    companies = []
    
    # Iterate through the input data
    for line in input_data:
        # Split the line into words
        words = line.split()
        
        # Get the company name and the packs it produces
        company_name = words[0]
        packs = []
        for i in range(1, len(words), 2):
            pack = {}
            pack["advertised_amount"] = int(words[i])
            pack["real_amount"] = int(words[i+1])
            packs.append(pack)
        
        # Add the company to the list of companies
        company = {}
        company["name"] = company_name
        company["packs"] = packs
        companies.append(company)
    
    # Return the list of companies
    return companies

def main():
    # Get the bolts needed and the number of companies
    bolts_needed, num_companies = map(int, input().split())
    
    # Get the companies
    companies = get_companies(input().split())
    
    # Get the smallest pack
    smallest_pack = get_smallest_pack(bolts_needed, companies)
    
    # Print the smallest pack
    print(smallest_pack)

if __name__ == '__main__':
    main()

