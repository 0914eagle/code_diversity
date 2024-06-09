
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    num_bottles1 = int(shipment_volume / bottle1_volume)
    num_bottles2 = int(shipment_volume / bottle2_volume)
    if num_bottles1 * bottle1_volume == shipment_volume and num_bottles2 * bottle2_volume == shipment_volume:
        return num_bottles1, num_bottles2
    else:
        return "Impossible"

def main():
    shipment_volume, bottle1_volume, bottle2_volume = map(int, input().split())
    print(get_bottles(shipment_volume, bottle1_volume, bottle2_volume))

if __name__ == '__main__':
    main()

