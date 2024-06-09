
def solve(poland_ball_words, enemy_ball_words):
    # Initialize a set to store the words known by PolandBall
    poland_ball_set = set(poland_ball_words)
    # Initialize a set to store the words known by EnemyBall
    enemy_ball_set = set(enemy_ball_words)
    # Find the intersection of the two sets
    common_words = poland_ball_set.intersection(enemy_ball_set)
    # If the intersection is empty, PolandBall wins
    if not common_words:
        return "YES"
    # If the intersection is not empty, EnemyBall wins
    else:
        return "NO"

