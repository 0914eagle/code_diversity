
def fibfib(n: int) -> int:
    
    if n <= 2:
        return n
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

