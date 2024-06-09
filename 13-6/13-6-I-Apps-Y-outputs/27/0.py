
def count_victims(snukes, snacks):
    victims = 0
    for i in range(len(snukes)):
        if not snukes[i]:
            victims += 1
    return victims

