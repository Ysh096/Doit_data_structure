A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4]
print(list(zip(A, B)))  # 범위를 벗어나면 무시됨, A의 마지막 원소 무시됨!
#[(1, 1), (2, 2), (3, 3), (4, 4)]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):  #p, c는 participant, completion의 각 원소
        if p != c:   #두 값이 같지 않으면
            return p #participant의 원소 반환
    return participant[-1] #끝까지 같다고 나오면, participant의 마지막 원소가 무시된 채로 zip이 수행된 것이다.
    #즉 participant[-1]이 완주하지 못한 선수이다.