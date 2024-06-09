
def restore_ipv6_address(short_address):
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

def main():
    num_addresses = int(input())
    for _ in range(num_addresses):
        short_address = input()
        full_address = restore_ipv6_address(short_address)
        print(full_address)

if __name__ == '__main__':
    main()

