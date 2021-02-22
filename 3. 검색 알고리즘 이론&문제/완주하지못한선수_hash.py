a = 'michael'
b = 'mi'
c = 'michael'
print(hash(a))  #89356~
print(hash(b))  #-4547~
print(hash(c))  #89356~
#hash함수를 사용하면 a, b, c 값에 대한 어떤 정수값을 만들어준다. 실행할때마다 달라짐.
#같은 값(a와 c)에 대해서는 같은 해시값을 가짐.
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:    #각 참가자에 대해
        dic[hash(part)] = part  #참가자의 해시값을 키로 하고, 참가자의 이름을 밸류로 하는 딕셔너리를 만든다.
        temp += hash(part)      #참가자의 해시값을 temp에 더해준다.
    for com in completion:      #각 완주자에 대해
        temp -= hash(com)       #완주자의 해시값을 temp에서 빼준다.
    answer = dic[temp]          #결과로 나오는 temp값은 어떤 이름의 hash값이 될 것이다.

    return answer