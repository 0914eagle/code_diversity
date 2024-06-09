
def determine_winner(poland_ball_words, enemy_ball_words):
    poland_ball_words = set(poland_ball_words)
    enemy_ball_words = set(enemy_ball_words)
    common_words = poland_ball_words.intersection(enemy_ball_words)
    if len(poland_ball_words - common_words) > len(enemy_ball_words - common_words):
        return "YES"
    else:
        return "NO"

