
def enlarge_article(article, z_r, z_c):
    return [[c * z_r * z_c for c in row] for row in article]

