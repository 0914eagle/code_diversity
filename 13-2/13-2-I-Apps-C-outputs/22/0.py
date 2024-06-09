
def solve(n, k):
    # Check if k is valid
    if k < 1 or k > n:
        return "NO"
    
    # Initialize the stations for Mobi and Vina
    mobi_stations = [i for i in range(1, n+1)]
    vina_stations = [i for i in range(1, n+1)]
    
    # Iterate through each pair of stations
    for i in range(n-1):
        for j in range(i+1, n):
            # Check if the stations are connected by both companies
            if mobi_stations[i] < mobi_stations[j] and vina_stations[i] < vina_stations[j]:
                return "NO"
    
    # If all conditions are satisfied, return the stations for Mobi and Vina
    return "YES\n" + "\n".join([f"{mobi_stations[i]} {mobi_stations[i+1]}" for i in range(k)]) + "\n" + "\n".join([f"{vina_stations[i]} {vina_stations[i+1]}" for i in range(k)])

