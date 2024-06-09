
def enlarge_article(article, z_r, z_c):
    return [[char * z_r for char in line] for line in article]

