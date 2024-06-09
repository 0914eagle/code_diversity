
def sand_consumption(upper_bulb_size, time_elapsed):
    return upper_bulb_size - (upper_bulb_size * time_elapsed / 100)

def main():
    upper_bulb_size, time_elapsed = map(int, input().split())
    print(sand_consumption(upper_bulb_size, time_elapsed))

if __name__ == '__main__':
    main()

