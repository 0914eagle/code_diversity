
def get_smallest_pack(bolts_needed, companies):
    # Initialize the smallest pack as impossible
    smallest_pack = -1
    
    # Loop through each company
    for company in companies:
        # Loop through each pack type offered by the company
        for pack_type in company:
            # Check if the pack type contains at least the number of bolts needed
            if pack_type >= bolts_needed:
                # If the pack type is smaller than the smallest pack found so far, update the smallest pack
                if smallest_pack == -1 or pack_type < smallest_pack:
                    smallest_pack = pack_type
                    break
    
    return smallest_pack

def main():
    # Read the input
    bolts_needed = int(input())
    companies = []
    for i in range(int(input())):
        companies.append(list(map(int, input().split())))
    
    # Get the smallest pack
    smallest_pack = get_smallest_pack(bolts_needed, companies)
    
    # Print the output
    if smallest_pack == -1:
        print("impossible")
    else:
        print(smallest_pack)

if __name__ == '__main__':
    main()

