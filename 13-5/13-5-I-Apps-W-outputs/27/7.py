
import re

def full_to_short(full_address):
    # Split the full address into blocks
    blocks = full_address.split(":")
    # Initialize an empty short address
    short_address = ""
    # Iterate over the blocks
    for block in blocks:
        # If the block is not all zeroes, add it to the short address
        if block != "0000":
            short_address += block + ":"
        # If the block is all zeroes, add a double colon to the short address
        else:
            short_address += "::"
    # Remove the trailing colon from the short address
    short_address = short_address[:-1]
    return short_address

def short_to_full(short_address):
    # Split the short address into blocks
    blocks = short_address.split(":")
    # Initialize an empty full address
    full_address = ""
    # Iterate over the blocks
    for block in blocks:
        # If the block is not all zeroes, add it to the full address
        if block != "0000":
            full_address += block + ":"
        # If the block is all zeroes, add a block of zeroes to the full address
        else:
            full_address += "0000:"
    # Remove the trailing colon from the full address
    full_address = full_address[:-1]
    return full_address

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        address = input()
        if re.search(r"::", address):
            print(short_to_full(address))
        else:
            print(full_to_short(address))

