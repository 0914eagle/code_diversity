
def calculate_inner_rating(displayed_rating, num_contests):
    if num_contests >= 10:
        return displayed_rating
    else:
        return displayed_rating + 100 * (10 - num_contests)

def main():
    num_contests, displayed_rating = map(int, input().split())
    inner_rating = calculate_inner_rating(displayed_rating, num_contests)
    print(inner_rating)

if __name__ == '__main__':
    main()

