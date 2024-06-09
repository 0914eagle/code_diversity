
def solve(poland_ball_words, enemy_ball_words):
    # Initialize a set to store the words known to Poland Ball
    poland_ball_set = set(poland_ball_words)
    # Initialize a set to store the words known to Enemy Ball
    enemy_ball_set = set(enemy_ball_words)
    # Initialize a variable to store the result
    result = "YES"

    # Iterate through the words known to Poland Ball
    for word in poland_ball_set:
        # If the word is not in the set of words known to Enemy Ball, then Poland Ball can say the word and Enemy Ball cannot say it
        if word not in enemy_ball_set:
            result = "NO"
            break

    return result

