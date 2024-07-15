# 백준에서는 넘파이를 못쓴다,, ~
import sys 

num = []
cnt = 1

for i in range(10) :
  num.append(int(sys.stdin.readline()) % 42)

num.sort()

for i in range(1, 10) :
  if num[i] != num[i-1] : cnt += 1

print(cnt)