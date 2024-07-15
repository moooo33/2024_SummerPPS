def roundUp(num) :
    if num - int(num) < 0.5:
        return int(num)
    else:
        return int(num)+1
        
days, feeling = map(int, input().split()) # type이 같은 경우 map으로 받는 게 더 유리!
prob = list(map(float, input().split()))
good, bad = 0, 0

if feeling == 0 : exp = [prob[0], prob[1]]  # good, bad
elif feeling == 1 : exp = [prob[2], prob[3]]

for i in range(days - 1) :
    new_exp = [exp[0] * prob[0], exp[0] * prob[1], exp[1] * prob[2], exp[1] * prob[3]]

    exp[0] = new_exp[0] + new_exp[2]
    exp[1] = new_exp[1] + new_exp[3]

print(roundUp(exp[0]*1000)) #파이썬에선 반올림 하려는 수가 올림, 내림했을 때 동일하게 차이가 나는 경우에는 짝수 값으로 반올림 
print(roundUp(exp[1]*1000))
