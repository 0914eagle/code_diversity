
def enlarge_article(article, z_r, z_c):
    return [[c * z_r * z_c for c in line] for line in article]

