# 윤년 ? 2월 29일 까지 있는 해 366일
# [1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31]

def solution(a, b):
    month_day = {
        1 : 31,
        2 : 29,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30, 
        10 : 31,
        11 : 30,
        12 : 31
    }
    date_day = {
        0 : 'THU',
        1 : 'FRI',
        2 : 'SAT',
        3 : 'SUN',
        4 : 'MON',
        5 : 'TUE',
        6 : 'WED'
    }
    toDate = 0
    for month in range(1, a) : 
        toDate += month_day.get(month)
    toDate += b
    
    date = date_day.get(toDate % 7)
    
    return date