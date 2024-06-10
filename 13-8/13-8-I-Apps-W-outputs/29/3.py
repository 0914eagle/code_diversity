
def get_max_birds(length, distance, num_birds):
    return int((length - num_birds * distance - 6) / (distance + 6))

def main():
    length, distance, num_birds = map(int, input().split())
    print(get_max_birds(length, distance, num_birds))

if __name__ == '__main__':
    main()

