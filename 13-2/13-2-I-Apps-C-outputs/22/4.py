
def solve(n, k):
    # Check if k is valid
    if k < 1 or k > n:
        return "NO"
    
    # Initialize the stations for Mobi and Vina
    mobi_stations = [i for i in range(1, n+1)]
    vina_stations = [i for i in range(1, n+1)]
    
    # Loop through each pair of stations
    for i in range(n):
        for j in range(i+1, n):
            # Check if the stations are connected by both companies
            if mobi_stations[i] < mobi_stations[j] and vina_stations[i] < vina_stations[j]:
                return "NO"
    
    # If we reach here, it is possible to satisfy all the conditions
    return "YES"

