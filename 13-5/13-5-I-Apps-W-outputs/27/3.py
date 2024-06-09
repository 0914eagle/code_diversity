
def restore_ipv6_address(short_address):
    full_address = []
    for block in short_address.split(":"):
        if block == "":
            full_address.append("0000")
        elif block == "0":
            full_address.append("0000")
        else:
            full_address.append(block.zfill(4))
    return ":".join(full_address)

def main():
    num_addresses = int(input())
    for _ in range(num_addresses):
        short_address = input()
        print(restore_ipv6_address(short_address))

if __name__ == '__main__':
    main()

