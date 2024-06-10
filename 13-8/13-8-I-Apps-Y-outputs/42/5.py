
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0
    else:
        worst_similar_movie = None
        for movie_1, movie_2 in similarities:
            if movie_1 == movie_id:
                if worst_similar_movie is None or similarities[(movie_1, movie_2)] > worst_similar_movie:
                    worst_similar_movie = similarities[(movie_1, movie_2)]
        if worst_similar_movie is None:
            return float('inf')
        else:
            return worst_similar_movie + 1

def solve(n, h, l, horror_list, similarities):
    horror_indices = [get_horror_index(i, horror_list, similarities) for i in range(n)]
    return max(range(n), key=lambda i: horror_indices[i])

if __name__ == '__main__':
    n, h, l = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = {}
    for _ in range(l):
        a, b = map(int, input().split())
        similarities[(a, b)] = 1
        similarities[(b, a)] = 1
    print(solve(n, h, l, horror_list, similarities))

