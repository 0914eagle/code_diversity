
def is_easy_enough(n, opinions):
    return "EASY" if all(opinion == 0 for opinion in opinions) else "HARD"

