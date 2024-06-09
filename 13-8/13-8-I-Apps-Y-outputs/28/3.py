
def get_midpoint(start_time, end_time):
    h1, m1 = map(int, start_time.split(':'))
    h2, m2 = map(int, end_time.split(':'))
    m_total = (h2 - h1) * 60 + (m2 - m1)
    m_mid = m_total // 2
    h_mid = h1 + m_mid // 60
    m_mid = m_mid % 60
    return f"{h_mid:02d}:{m_mid:02d}"

