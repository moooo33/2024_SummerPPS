import sys
sum = 0
num = int(sys.stdin.readline())
for i in range(num-1) :
    cnt = int(sys.stdin.readline()) - 1
    sum += cnt
cnt = int(sys.stdin.readline())
sum += cnt
print(sum)