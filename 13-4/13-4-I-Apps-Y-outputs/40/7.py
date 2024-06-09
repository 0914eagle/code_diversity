
def enlarge_article(R, C, Z_R, Z_C):
    article = []
    for i in range(R):
        article.append(input())
    
    enlarged_article = []
    for i in range(R*Z_R):
        enlarged_article.append(['' for j in range(C*Z_C)])
    
    for i in range(R):
        for j in range(C):
            char = article[i][j]
            for k in range(Z_R):
                for l in range(Z_C):
                    enlarged_article[i*Z_R+k][j*Z_C+l] = char
    
    return enlarged_article

