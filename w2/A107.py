s, e = map(int, input().split())
seq = []
for i in range(1, e+1) :
  for j in range(i) :
    seq.append(i)

print(sum(seq[s-1:e]))