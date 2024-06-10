
def get_inner_rating(contests, displayed_rating):
    if contests >= 10:
        return displayed_rating
    else:
        return displayed_rating + (100 * (10 - contests))

def main():
    contests, displayed_rating = map(int, input().split())
    print(get_inner_rating(contests, displayed_rating))

if __name__ == '__main__':
    main()

