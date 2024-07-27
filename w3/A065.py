# 파이썬은 앞, 뒤 순서대로 자동정렬 해줌
num = int(input())
points = []

for i in range(num) :
  x, y = map(int, input().split())
  points.append((x, y))

points.sort()
for i in points : print(i[0], i[1])