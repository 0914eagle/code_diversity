
def get_rating_after_contest(current_rating, performance):
    return (current_rating + performance) / 2

def get_performance_required(current_rating, desired_rating):
    return (desired_rating * 2) - current_rating

if __name__ == '__main__':
    current_rating = int(input())
    desired_rating = int(input())
    print(get_performance_required(current_rating, desired_rating))

