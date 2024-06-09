
def get_full_address(short_address):
    full_address = ""
    for block in short_address.split(":"):
        if block == "":
            full_address += "0000"
        elif block == "0":
            full_address += "0000"
        else:
            full_address += block.zfill(4)
    return full_address

def get_short_address(full_address):
    short_address = ""
    for block in full_address.split(":"):
        if block == "0000":
            short_address += ":"
        else:
            short_address += block
    return short_address

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        short_address = input()
        full_address = get_full_address(short_address)
        print(full_address)

