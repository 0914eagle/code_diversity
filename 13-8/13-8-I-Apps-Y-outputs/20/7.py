
def get_inner_rating(num_contests, displayed_rating):
    if num_contests >= 10:
        return displayed_rating
    else:
        return displayed_rating + (100 * (10 - num_contests))

def main():
    num_contests, displayed_rating = map(int, input().split())
    print(get_inner_rating(num_contests, displayed_rating))

if __name__ == '__main__':
    main()

