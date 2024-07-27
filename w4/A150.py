num = int(input())
line = input().split()
max_sum = int(line[0])
temp = 0

for i in range(num) :
  temp += int(line[i])
  if temp > max_sum :
    max_sum = temp
  if temp < 0 :
    temp = 0

print(max_sum)