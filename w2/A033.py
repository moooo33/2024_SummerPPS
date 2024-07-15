score = []
for i in range(5) : 
  grad = list(map(int, input().split()))
  score.append(sum(grad))
  
print(score.index(max(score))+1, max(score))