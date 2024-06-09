
def count_victims(snakes, snacks):
    victims = 0
    for snake in snakes:
        if not set(snake).intersection(snacks):
            victims += 1
    return victims

