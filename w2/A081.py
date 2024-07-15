import sys

num = int(sys.stdin.readline())

for i in range(num) :
  inp = list(map(int, input().split()))
  inp.sort(reverse=True)
  print(inp[2])