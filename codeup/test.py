def solution(people, limit):
    answer = 0
    # 우선 정렬해서 가장 가벼운 녀석과 가장 무거운 녀석을 태워본다
    people.sort()
    # 리스트 길이가 0 될때까지
    while people:
        # 만약 가장 가벼운 녀석과 가장 무거운 녀석 무게합이 리미트를 넘으면
        # 무게 제한은 몸무게 최대값보단 크니까 큰 녀석만 일단 탈출
        if people[0] + people[-1] > limit:
            answer += 1
            people.pop()
        # 가벼운 녀석과 무거운 녀석 둘 다 탈 수 있으면
        else:
            # 둘 다 태워 보낸다
            answer += 1
            people.pop(0)
            people.pop()

    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))