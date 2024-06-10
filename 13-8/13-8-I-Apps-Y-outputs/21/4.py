
def get_rating_requirement(current_rating, desired_rating):
    return (desired_rating + current_rating) / 2

def get_performance_requirement(current_rating, desired_rating):
    return get_rating_requirement(current_rating, desired_rating) - current_rating

if __name__ == '__main__':
    current_rating, desired_rating = map(int, input().split())
    print(get_performance_requirement(current_rating, desired_rating))

