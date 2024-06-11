def histogram(test):
    
    if not test:
        return {}
    return Counter(test.split())


