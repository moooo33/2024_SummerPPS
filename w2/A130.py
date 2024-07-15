ele = []
num = int(input())

for i in range(num) : 
  temp = int(input())
  if (temp == 0) : ele.pop()
  else : ele.append(temp)

print(sum(ele))