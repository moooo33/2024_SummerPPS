names = {}
rtn = []
num = int(input())
for i in range(num) : 
  player = input()
  if player[0] in names : 
    names[player[0]] += 1
  else : names[player[0]] = 1

names = sorted(names.items())
# print(names)
if len(names) < 5 : print("PREDAJA")
else : 
  for i in names : 
    # print(i[0])
    if i[1] >= 5 : rtn.append(i[0])

rtn = sorted(rtn)
print(''.join(rtn))
