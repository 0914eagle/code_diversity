
def get_tall_friends(heights, min_height):
    return len([h for h in heights if h >= min_height])

def main():
    num_friends, min_height = map(int, input().split())
    heights = list(map(int, input().split()))
    print(get_tall_friends(heights, min_height))

if __name__ == '__main__':
    main()

