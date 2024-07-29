A = input()
B = input()

len_a = len(A)
len_b = len(B)

dp = [[0 for _ in range(len_b)] for _ in range(len_a)]

dp [0][0] = 1 if A[0]==B[0] else 0

for i in range(len_a):
    for j in range(len_b):
        if (i == 0 and j !=0) or (i!=0 and j==0) :
            if A[i] == B[j] :
                dp[i][j] = 1
            else :
                dp[i][j] = 0

        elif i !=0 and j !=0 :
            if A[i] == B[j]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
            else :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len_a-1][len_b-1])