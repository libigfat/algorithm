import numpy as np

'''
题目：给出三个字符串s1、s2、s3，判断s3是否由s1和s2交叉构成
组合过程不能改变字符在s1，s2字符串中的原本顺序
若是则输出为TRUE,若不是则输出为FALSE
'''
'''
思路：动态规划求解，构造一个长为len2=len(s2)+1，宽为len1=len(s1)+1的二维数组dp[][]
设i、j，其中i表示字符串s1的第i个字符，j表示字符串s2的第j个字符，t=i+j表示s3的第t个字符
如果dp[i][j]为1，表示s1[i]等于s3[t]且dp[i−1][j]为1，或者s2[j]等于s3[t]且dp[i][j−1]为1
dp[i][j]为1表示这个点可达，以dp[0][0]为起点，dp[len(s1)][len(s2)]为终点
dp[i][j]中为1的点组合成路径，向下走表示取s1的字符，向右走表示取s2的字符
dp[len(s1)][len(s2)]是否为1，终点是否可达，判断s3是否由s1和s2交叉构成
'''

s1 = 'dbf'
s2 = 'aba'
s3 = 'abdbaf'


def test_str(s1, s2, s3):
    len1 = len(s1)
    len2 = len(s2)
    len3 = len(s3)

    if len3 != len1 + len2:
        return False

    if len1 == 0:
        return s2 == s3

    if len2 == 0:
        return s1 == s3

    dp = np.zeros([len1 + 1, len2 + 1])
    dp[0, 0] = 1

    for i in range(1, len1 + 1):
        if s1[i - 1] == s3[i - 1]:
            dp[i, 0] = dp[i - 1, 0]

    for j in range(1, len2 + 1):
        if s2[j - 1] == s3[j - 1]:
            dp[0, j] = dp[0, j - 1]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            t = i + j
            if s1[i - 1] == s3[t - 1]:
                dp[i, j] = dp[i - 1, j]

            if s2[j - 1] == s3[t - 1]:
                dp[i, j] = dp[i, j - 1] or dp[i, j]

    print(dp)

    if dp[len1, len2] == 1:
        return True
    return False


result = test_str(s1, s2, s3)
print(result)
