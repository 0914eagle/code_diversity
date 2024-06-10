
def calculate_inner_rating(participations, displayed_rating):
    if participations >= 10:
        return displayed_rating
    else:
        return displayed_rating + 100 * (10 - participations)

def main():
    participations, displayed_rating = map(int, input().split())
    inner_rating = calculate_inner_rating(participations, displayed_rating)
    print(inner_rating)

if __name__ == '__main__':
    main()

