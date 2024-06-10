
def get_min_difficulty(n, k, courses):
    # Initialize a dictionary to store the course names and their difficulties
    course_dict = {}
    for course in courses:
        course_name, difficulty = course.split()
        course_dict[course_name] = int(difficulty)

    # Initialize a graph to store the course dependencies
    graph = {}
    for course in courses:
        course_name, difficulty = course.split()
        graph[course_name] = []

    # Populate the graph with the course dependencies
    for course in courses:
        course_name, difficulty = course.split()
        if course_name.endswith("1"):
            graph[course_name].append(course_name[:-1] + "2")
        elif course_name.endswith("2"):
            graph[course_name].append(course_name[:-1] + "1")

    # Find the minimum difficulty path using Dijkstra's algorithm
    min_difficulty_path = dijkstra(graph, "linearalgebra", k)

    # Calculate the minimum difficulty sum
    min_difficulty_sum = 0
    for course in min_difficulty_path:
        min_difficulty_sum += course_dict[course]

    return min_difficulty_sum

def dijkstra(graph, start, target):
    # Initialize the minimum distance dictionary
    min_distance = {}
    for course in graph:
        min_distance[course] = float("inf")
    min_distance[start] = 0

    # Initialize the previous course dictionary
    previous_course = {}
    for course in graph:
        previous_course[course] = None

    # Initialize the queue with the starting course
    queue = [start]

    while queue:
        # Get the current course from the queue
        current_course = queue.pop(0)

        # If the current course is the target course, return the path
        if current_course == target:
            path = [current_course]
            while previous_course[current_course] is not None:
                path.append(previous_course[current_course])
            path.reverse()
            return path

        # If the current course has not been visited before, visit it
        if min_distance[current_course] != float("inf"):
            for neighbor in graph[current_course]:
                new_distance = min_distance[current_course] + 1
                if new_distance < min_distance[neighbor]:
                    min_distance[neighbor] = new_distance
                    previous_course[neighbor] = current_course
                    queue.append(neighbor)

    return []

def main():
    n, k = map(int, input().split())
    courses = []
    for i in range(n):
        course = input()
        courses.append(course)
    print(get_min_difficulty(n, k, courses))

if __name__ == "__main__":
    main()

