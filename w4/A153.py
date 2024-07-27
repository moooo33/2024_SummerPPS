num = int(input())
line = list(map(int, input().split()))

line.sort()  
total_time = 0  

for x in range(1, num+1):
  total_time += sum(line[0:x])  
  
print(total_time)  