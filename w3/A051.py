num = input()
sum = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in num :
  for j in dial : 
    if i in j : sum += dial.index(j) + 3

print(sum)
