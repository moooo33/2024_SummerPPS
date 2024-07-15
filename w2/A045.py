import sys

str = sys.stdin.readline()
str = str[:-1].upper()
str_list = list(str)
dict = {} # 딕셔너리로 저장

for i in range(len(str_list)) :
  if str_list[i] not in dict : 
    dict[str_list[i]] = 1
  else : dict[str_list[i]] += 1

dict = sorted(dict.items(), key=lambda x: x[1], reverse=True) # dictionary sorting

if len(dict) == 1 : print(dict[0][0])
elif dict[0][1] == dict[1][1] : print("?")
else : print(dict[0][0])