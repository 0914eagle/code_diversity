
def get_midpoint(start_time, end_time):
    h1, m1 = map(int, start_time.split(':'))
    h2, m2 = map(int, end_time.split(':'))
    total_minutes = (h2 - h1) * 60 + (m2 - m1)
    midpoint_minutes = total_minutes // 2
    h3 = midpoint_minutes // 60
    m3 = midpoint_minutes % 60
    return f"{h3:02d}:{m3:02d}"

