
def get_performance(current_rating, goal_rating):
    return (goal_rating + current_rating) / 2

def main():
    current_rating, goal_rating = map(int, input().split())
    print(get_performance(current_rating, goal_rating))

if __name__ == '__main__':
    main()

