
def read_input():
    n, k = map(int, input().split())
    courses = {}
    for _ in range(n):
        name, difficulty = input().split()
        courses[name] = int(difficulty)
    return n, k, courses

def f1(n, k, courses):
    # create a graph with courses as nodes and edges between courses with same name but different levels
    graph = {}
    for course, difficulty in courses.items():
        name = course.split('1')[0]
        if name not in graph:
            graph[name] = []
        graph[name].append((course, difficulty))
    
    # find the minimum spanning tree of the graph
    mst = []
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor, difficulty in graph[node]:
            mst.append((neighbor, difficulty))
            dfs(neighbor)
    
    for node in graph:
        dfs(node)
    
    # calculate the minimum sum of difficulties of the k courses
    total_difficulty = 0
    for i in range(k):
        total_difficulty += mst[i][1]
    
    return total_difficulty

def f2(n, k, courses):
    # create a list of courses with levels and difficulties
    courses_with_levels = []
    for course, difficulty in courses.items():
        if course.endswith('1'):
            courses_with_levels.append((course, difficulty, 1))
        elif course.endswith('2'):
            courses_with_levels.append((course, difficulty, 2))
    
    # sort the courses by difficulty in ascending order
    courses_with_levels.sort(key=lambda x: x[1])
    
    # take the first k courses with levels 1 and the first k-1 courses with levels 2
    total_difficulty = 0
    for i in range(k):
        total_difficulty += courses_with_levels[i][1]
    for i in range(k, len(courses_with_levels)):
        if courses_with_levels[i][2] == 2:
            total_difficulty += courses_with_levels[i][1]
    
    return total_difficulty

if __name__ == '__main__':
    n, k, courses = read_input()
    print(f1(n, k, courses))
    print(f2(n, k, courses))

