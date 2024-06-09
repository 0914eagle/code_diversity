
def get_boss_and_subordinates(employees, query):
    # Initialize the boss and subordinates for the query employee
    boss, subordinates = None, 0
    
    # Iterate through the employees
    for employee in employees:
        # If the query employee is taller than the current employee and earns more than the current employee, set the current employee as the boss
        if query[1] > employee[1] and query[2] > employee[2]:
            boss = employee
        # If the query employee is the boss of the current employee, increment the subordinates count
        elif employee[0] == query[0]:
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
    for _ in range(q):
        query = list(map(int, input().split()))
        
        # Get the boss and subordinates for the query employee
        boss, subordinates = get_boss_and_subordinates(employees, query)
        
        # Print the boss and subordinates for the query employee
        print(boss[0] if boss else 0, subordinates)

if __name__ == '__main__':
    main()

