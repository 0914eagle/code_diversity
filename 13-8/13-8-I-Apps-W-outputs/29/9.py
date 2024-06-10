
def get_max_birds(length, distance, number_of_birds):
    return int((length - (number_of_birds * distance)) / distance)

def main():
    length, distance, number_of_birds = map(int, input().split())
    print(get_max_birds(length, distance, number_of_birds))

if __name__ == '__main__':
    main()

