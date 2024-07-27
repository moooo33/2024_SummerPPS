num = int(input())
li = []
dp = [[0] * num for _ in range(num)]
for i in range(num):
    li.append(list(map(int, input().split())))

dp[0][0] = li[0][0]

for i in range(1, num):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + li[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + li[i][j]

print(max(dp[num-1]))