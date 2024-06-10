
def get_number_of_balls(n, balls):
    return sum(balls)

def get_number_of_colors(n, colors):
    return len(set(colors))

def get_number_of_unallowed_colors(n, unallowed_colors):
    return len(set(unallowed_colors))

def get_favorite_sequence(n, favorite_sequence):
    return " ".join(str(x) for x in favorite_sequence)

def get_number_of_favorite_sequence_occurrences(n, favorite_sequence):
    return favorite_sequence.count(favorite_sequence[0])

def get_number_of_arrangements(n, balls, colors, unallowed_colors, favorite_sequence):
    number_of_balls = get_number_of_balls(n, balls)
    number_of_colors = get_number_of_colors(n, colors)
    number_of_unallowed_colors = get_number_of_unallowed_colors(n, unallowed_colors)
    favorite_sequence = get_favorite_sequence(n, favorite_sequence)
    number_of_favorite_sequence_occurrences = get_number_of_favorite_sequence_occurrences(n, favorite_sequence)
    
    # Implement your algorithm here
    return 0

if __name__ == '__main__':
    n = int(input())
    balls = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    unallowed_colors = list(map(int, input().split()))
    favorite_sequence = list(map(int, input().split()))
    print(get_number_of_arrangements(n, balls, colors, unallowed_colors, favorite_sequence))

