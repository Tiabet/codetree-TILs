A = input()
B = input()

len_a = len(A)
len_b = len(B)

# Initialize the dp table
dp = [[0 for _ in range(len_b)] for _ in range(len_a)]

# Initialize the first row and first column of the dp table
if A[0] == B[0]:
    dp[0][0] = 1

for i in range(1, len_a):
    dp[i][0] = dp[i-1][0] if A[i] != B[0] else 1

for j in range(1, len_b):
    dp[0][j] = dp[0][j-1] if B[j] != A[0] else 1

# Fill the dp table
for i in range(1, len_a):
    for j in range(1, len_b):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# The length of the longest common subsequence is in the bottom-right cell of the dp table
print(dp[len_a-1][len_b-1])