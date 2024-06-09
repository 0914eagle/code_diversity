
def get_smallest_pack(B, k, companies):
    # Initialize the smallest pack as impossible
    smallest_pack = "impossible"
    
    # Loop through each company
    for i in range(k):
        # Get the number of packages and their sizes for this company
        num_packages, packages = companies[i]
        
        # Loop through each package size
        for j in range(num_packages):
            # Check if the package size is greater than or equal to the number of bolts needed
            if packages[j] >= B:
                # If the smallest pack is still impossible, set it to this package size
                if smallest_pack == "impossible":
                    smallest_pack = packages[j]
                # If the package size is less than the smallest pack, set the smallest pack to this package size
                elif packages[j] < smallest_pack:
                    smallest_pack = packages[j]
    
    # Return the smallest pack
    return smallest_pack

def main():
    # Read the number of bolts and the number of companies
    B, k = map(int, input().split())
    
    # Read the companies and their packages
    companies = []
    for i in range(k):
        num_packages, packages = map(int, input().split())
        companies.append((num_packages, packages))
    
    # Get the smallest pack
    smallest_pack = get_smallest_pack(B, k, companies)
    
    # Print the smallest pack
    print(smallest_pack)

if __name__ == '__main__':
    main()

