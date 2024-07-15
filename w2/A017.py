rnum = input("")
cnt = [0,0,0,0,0,0,0,0,0,0]

for i in rnum : 
  if int(i) == 6 or int(i) == 9 :
    if cnt[6] <= cnt[9] :
      cnt[6] += 1
    else : cnt[9] += 1
  else : cnt[int(i)] += 1
  
# 6, 9는 뒤집어서 쓸 수 있음
#  => 개수가 작은 걸 증가
cnt.sort(reverse=True)
print(cnt[0])