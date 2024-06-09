
def get_maximum_bouquets(r, g, b):
    red_bouquets = r // 3
    green_bouquets = g // 3
    blue_bouquets = b // 3
    mixing_bouquets = min(red_bouquets, green_bouquets, blue_bouquets)
    return red_bouquets + green_bouquets + blue_bouquets + mixing_bouquets

def main():
    r, g, b = map(int, input().split())
    print(get_maximum_bouquets(r, g, b))

if __name__ == '__main__':
    main()

