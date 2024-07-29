A = input()
B = input()

len_a = len(A)
len_b = len(B)

dp = [[0 for _ in range(len_b)] for _ in range(len_a)]

dp[0][0] = 1 if A[0]==B[0] else 0

for i in range(1,len_a):
    if A[i]== B[0]:
        for j in range(i,len_a):
            dp[j][0] = 1

for i in range(1,len_b):
    if B[i] == A[0] :
        for j in range(i,len_b):
            dp[0][j] = 1

for i in range(1,len_a):
    for j in range(1,len_b):
        if A[i] == B[j]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[len_a-1][len_b-1])