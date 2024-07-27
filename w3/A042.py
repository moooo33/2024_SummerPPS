# 공백 때문에 틀려서 화가 났다 
# 이유를 전혀 모르겠으면 질문 게시판을 잘 보기 ~
def solution(s):

    S = s.lower()
    H = S.split(' ')
    STRING = []

    for i in H:
        print(i)
        if i:
            Z = i[0].upper() + i[1:]
        else:
            Z = i
        STRING.append(Z)
    last = ' '.join(STRING)

    return last