
def enlarge_article(article, z_r, z_c):
    enlarged_article = []
    for row in article:
        enlarged_row = []
        for char in row:
            enlarged_row += [char] * z_c
        enlarged_article += [enlarged_row] * z_r
    return enlarged_article

