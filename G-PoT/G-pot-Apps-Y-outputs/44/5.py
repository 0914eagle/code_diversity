
def calculate_min_scientists_to_bribe(articles, impact_factor):
    total_citations_needed = articles * impact_factor
    total_citations_current = 0
    scientists_bribed = 0
    
    while total_citations_current < total_citations_needed:
        total_citations_current += articles
        scientists_bribed += 1
    
    return scientists_bribed

# Read input
articles, impact_factor = map(int, input().split())

# Calculate and output result
result = calculate_min_scientists_to_bribe(articles, impact_factor)
print(result)
