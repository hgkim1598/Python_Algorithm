def solution(a, b):
    day_of_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']  # day_of_week[1]이 금요일이 되도록 맞춰줌
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 달의 일 수
    
    day = sum(months[:a-1])+b  # 1월 부터 a-1월 까지의 일수를 더하고 거기에 b일을 더해준다
    answer = day_of_week[(day%7)]  # day를 7로 나눈 나머지번째 요일을 가져온다
    return answer