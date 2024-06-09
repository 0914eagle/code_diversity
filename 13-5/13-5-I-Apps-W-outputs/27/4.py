
def full_ipv6_address(short_address):
    full_address = ""
    blocks = short_address.split(":")
    for block in blocks:
        if len(block) == 0:
            full_address += "0000"
        elif len(block) == 1:
            full_address += "000" + block
        elif len(block) == 2:
            full_address += "00" + block
        elif len(block) == 3:
            full_address += "0" + block
        else:
            full_address += block
    return full_address

def shorten_zero_blocks(full_address):
    short_address = ""
    blocks = full_address.split(":")
    for block in blocks:
        if block == "0000":
            short_address += ":"
        else:
            short_address += block + ":"
    return short_address[:-1]

def restore_full_address(short_address):
    full_address = full_ipv6_address(short_address)
    return shorten_zero_blocks(full_address)

if __name__ == '__main__':
    num_addresses = int(input())
    for _ in range(num_addresses):
        short_address = input()
        print(restore_full_address(short_address))

