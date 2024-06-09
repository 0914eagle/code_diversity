
def get_performance(current_rating, desired_rating):
    return (desired_rating + current_rating) / 2

def main():
    current_rating, desired_rating = map(int, input().split())
    print(get_performance(current_rating, desired_rating))

if __name__ == '__main__':
    main()

