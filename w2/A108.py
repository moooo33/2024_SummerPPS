import sys

num = int(sys.stdin.readline())
isEqual = []

for i in range(num) :
  reverse = ''
  origin = sys.stdin.readline()
  origin = origin[:-1] # \n은 한 글자로 친다네요~
  
  # 배열 역순출력 1
  # for j in range(len(origin)-1, -1, -1) :
  #   reverse += origin[j]
  # 배열 역순출력 2
  reverse = origin[::-1]
  sum = str(int(origin) + int(reverse))
  isEqual.append(sum == sum[::-1])

for i in isEqual :
  if i : print('YES')
  else : print('NO')