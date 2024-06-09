
def solve(poland_ball_words, enemy_ball_words):
    poland_ball_words = set(poland_ball_words)
    enemy_ball_words = set(enemy_ball_words)
    return "YES" if len(poland_ball_words - enemy_ball_words) > 0 else "NO"

