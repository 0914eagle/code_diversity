
def get_rating_change(current_rating, new_rating):
    return (current_rating + new_rating) / 2

def get_performance_required(current_rating, desired_rating):
    return desired_rating - current_rating

if __name__ == '__main__':
    current_rating = int(input())
    desired_rating = int(input())
    print(get_performance_required(current_rating, desired_rating))

