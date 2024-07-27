K, N = map(int, input().split())
lan = list(map(int, input().split()))
start, end = 1, max(lan) 

while start <= end : 
    mid = (start + end) 
    lines = 0 
    for i in lan :
        lines += i 
        
    if lines >= N : 
        start = mid + 1
    else:
        end = mid - 1

print(end)