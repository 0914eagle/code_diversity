
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    num_bottles1 = 0
    num_bottles2 = 0
    while shipment_volume > 0:
        if shipment_volume >= bottle1_volume:
            num_bottles1 += 1
            shipment_volume -= bottle1_volume
        else:
            num_bottles2 += 1
            shipment_volume -= bottle2_volume
    return num_bottles1, num_bottles2

def main():
    shipment_volume, bottle1_volume, bottle2_volume = map(int, input().split())
    num_bottles1, num_bottles2 = get_bottles(shipment_volume, bottle1_volume, bottle2_volume)
    if num_bottles1 == 0 and num_bottles2 == 0:
        print("Impossible")
    else:
        print(num_bottles1, num_bottles2)

if __name__ == '__main__':
    main()

