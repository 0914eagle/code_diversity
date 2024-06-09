
def restore_ipv6_address(short_address):
    full_address = ""
    blocks = short_address.split(":")
    for block in blocks:
        if block == "":
            full_address += ":0000"
        elif block == "0":
            full_address += ":0000"
        else:
            full_address += ":" + block
    return full_address[1:]

def main():
    n = int(input())
    for i in range(n):
        short_address = input()
        full_address = restore_ipv6_address(short_address)
        print(full_address)

if __name__ == '__main__':
    main()

