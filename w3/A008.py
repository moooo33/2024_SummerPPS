nums = int(input())
for i in range(nums) : 
    cnt = 0
    line = [int(j) for j in input().split()]
    avg = sum(line[1:]) / line[0]
    # print(avg)
    for j in line[1:] :
        if j > avg : cnt += 1
    print(f'{round(cnt / line[0] * 100, 3):.3f}%') # format 대신 f-string 사용