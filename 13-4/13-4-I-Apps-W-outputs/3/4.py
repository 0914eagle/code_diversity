
def get_guardpost(n, guardposts):
    for guardpost in guardposts:
        chocolate_cost = guardpost[0]
        juice_cost = guardpost[1]
        if chocolate_cost + juice_cost == n:
            return guardpost
    return -1

