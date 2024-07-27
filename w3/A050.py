num = input()
rtn = ''

for i in num : 
  if (ord(i) >= ord('D')) and (ord(i) <= ord('Z')) :
    rtn += chr(ord(i) - 3)
  elif (ord(i) <= ord('C')) and (ord(i) >= ord('A')) :
    rtn += chr(ord(i) + 23)

print(rtn)