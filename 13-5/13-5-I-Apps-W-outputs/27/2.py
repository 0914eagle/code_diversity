
def full_ipv6_address(short_address):
    full_address = ""
    blocks = short_address.split(":")
    for block in blocks:
        if block == "":
            full_address += ":0000"
        elif len(block) == 1:
            full_address += ":000" + block
        elif len(block) == 2:
            full_address += ":00" + block
        elif len(block) == 3:
            full_address += ":0" + block
        elif len(block) == 4:
            full_address += ":" + block
    return full_address[1:]

def short_ipv6_address(full_address):
    short_address = ""
    blocks = full_address.split(":")
    for block in blocks:
        if block == "0000":
            short_address += ":"
        elif block == "00000000":
            short_address += "::"
        else:
            short_address += ":" + block
    return short_address[1:]

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        short_address = input()
        full_address = full_ipv6_address(short_address)
        print(full_address)

