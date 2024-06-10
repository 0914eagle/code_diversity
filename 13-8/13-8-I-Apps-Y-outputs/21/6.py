
def get_performance(rating, goal):
    return (goal - rating) / 2 + rating

def main():
    rating, goal = map(int, input().split())
    print(get_performance(rating, goal))

if __name__ == '__main__':
    main()

