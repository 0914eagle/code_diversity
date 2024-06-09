
def solve(poland_ball_words, enemy_ball_words):
    # Initialize a set to store the words known by PolandBall
    poland_ball_set = set(poland_ball_words)
    # Initialize a set to store the words known by EnemyBall
    enemy_ball_set = set(enemy_ball_words)
    # Initialize a variable to store the result
    result = "YES"

    # Iterate through the words known by PolandBall
    for word in poland_ball_set:
        # If the word is not in the set of words known by EnemyBall, then PolandBall can say the word and EnemyBall will not be able to respond
        if word not in enemy_ball_set:
            result = "NO"
            break

    # Return the result
    return result

