
def get_boss_and_subordinates(employees, query):
    # Initialize the boss and subordinates for the query employee
    boss, subordinates = None, 0
    
    # Iterate through the employees
    for employee in employees:
        # If the employee is the query employee, set the boss and subordinates
        if employee[0] == query:
            boss = employee[1]
            subordinates = employee[2]
            break
    
    # If the employee is not the query employee, check if they are the boss of the query employee
        elif employee[1] == query:
            boss = employee[0]
            subordinates += 1
    
    # Return the boss and subordinates for the query employee
    return boss, subordinates

def main():
    # Read the number of employees and queries
    m, q = map(int, input().split())
    
    # Read the employees
    employees = []
    for _ in range(m):
        employees.append(list(map(int, input().split())))
    
    # Read the queries
    queries = []
    for _ in range(q):
        queries.append(int(input()))
    
    # Iterate through the queries
    for query in queries:
        # Get the boss and subordinates for the query employee
        boss, subordinates = get_boss_and_subordinates(employees, query)
        
        # Print the boss and subordinates for the query employee
        print(boss, subordinates)

if __name__ == '__main__':
    main()

