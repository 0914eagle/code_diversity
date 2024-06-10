
def get_rating(performance, current_rating):
    return (current_rating + performance) / 2

def get_performance(desired_rating, current_rating):
    return desired_rating * 2 - current_rating

if __name__ == '__main__':
    current_rating = int(input())
    desired_rating = int(input())
    performance = get_performance(desired_rating, current_rating)
    print(performance)

