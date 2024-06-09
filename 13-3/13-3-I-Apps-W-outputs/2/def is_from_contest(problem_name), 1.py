
def is_from_contest(problem_name):
    friends = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
    for friend in friends:
        if problem_name.count(friend) == 1:
            return "YES"
    return "NO"

