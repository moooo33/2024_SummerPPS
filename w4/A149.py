num = int(input())
person = []
rtn = []

for i in range(num) : 
  x, y = map(int, input().split())
  person.append((x, y))

for i in range(num):
  count = 0
  for j in range(num):
      if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
          count += 1 
  rtn.append(str(count + 1)) 

print(" ".join(rtn))
