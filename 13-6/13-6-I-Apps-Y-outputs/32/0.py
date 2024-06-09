
def enlarge_article(R, C, Z_R, Z_C, article):
    enlarged_article = []
    for i in range(R):
        enlarged_row = []
        for j in range(C):
            char = article[i][j]
            if char == '.':
                enlarged_row += [''] * (Z_C - 1)
            else:
                enlarged_row += [char] * Z_C
        enlarged_article.append(enlarged_row)
    return enlarged_article

