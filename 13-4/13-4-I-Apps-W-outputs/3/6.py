
def get_rooted_dead_bush(n):
    if n == 1 or n == 2:
        return 0
    
    # Initialize the RDB with a root vertex and no children
    rdb = [1]
    
    # Construct the RDB by adding vertices and edges
    for i in range(2, n+1):
        new_rdb = []
        for vertex in rdb:
            if vertex not in new_rdb:
                new_rdb.append(vertex)
                if len(new_rdb) == 1:
                    new_rdb.append(vertex+1)
                elif len(new_rdb) == 2:
                    new_rdb.append(vertex+1)
                    new_rdb.append(vertex+2)
        rdb = new_rdb
    
    # Find all possible claws in the RDB
    claws = []
    for i in range(len(rdb)):
        for j in range(i+1, len(rdb)):
            for k in range(j+1, len(rdb)):
                if rdb[i] == rdb[j] and rdb[j] == rdb[k]:
                    claws.append([rdb[i], rdb[j], rdb[k], rdb[i]+1])
    
    # Count the number of yellow vertices
    yellow_vertices = 0
    for claw in claws:
        if all(vertex in rdb for vertex in claw) and claw[0] == claw[3]:
            yellow_vertices += 1
    
    return yellow_vertices % (10**9 + 7)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_rooted_dead_bush(n))

if __name__ == '__main__':
    main()

