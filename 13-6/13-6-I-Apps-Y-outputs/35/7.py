
def get_sand_amount(upper_bulb_size, time_passed):
    return upper_bulb_size - time_passed

def main():
    upper_bulb_size, time_passed = map(int, input().split())
    print(get_sand_amount(upper_bulb_size, time_passed))

if __name__ == '__main__':
    main()

