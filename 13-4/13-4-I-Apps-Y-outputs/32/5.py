
def get_non_similar_keywords(keywords):
    # Convert all keywords to lowercase and remove hyphens
    keywords = [keyword.lower().replace("-", "") for keyword in keywords]
    
    # Create a set to store unique keywords
    unique_keywords = set()
    
    # Iterate over the keywords
    for keyword in keywords:
        # Check if the keyword is already in the set
        if keyword not in unique_keywords:
            # If not, add it to the set
            unique_keywords.add(keyword)
    
    # Return the length of the set
    return len(unique_keywords)

