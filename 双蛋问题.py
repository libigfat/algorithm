import numpy as np

'''
题目：你将获得K个鸡蛋，并可以使用一栋从1到N共有N层楼的建筑
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去
你知道存在楼层F，满足0<=F<=N任何从高于F的楼层落下的鸡蛋都会碎
从F楼层或比它低的楼层落下的鸡蛋都不会破
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）
并把它从任一楼层X扔下（满足1<=X<=N）
你的目标是确切地知道F的值是多少
无论F的初始值如何，你确定F的值的最小移动次数是多少
'''
'''
思路：1.动态规划求解，构造一个长为N+1，宽为K+1的二维数组dp[][]
状态可以表示成dp[K][N]，其中K为鸡蛋数，N为楼层数
从第X楼扔鸡蛋：鸡蛋碎了，dp[K-1][X-1]；鸡蛋不碎，dp[K][N-X]
dp[K][N]=1+min(max(dp[K-1][X-1],dp[K][N-X])，1<=X<=N)
最坏情况的最小值
2.动态规划加二分法，减少复杂度
dp[K][N]是一个关于N的单调递增函数
鸡蛋数K固定的情况下，楼层数N越多，需要的步数一定不会变少
dp[K-1][X-1]是一个随X的增加而单调递增的函数
dp[K][N-X]是一个随X的增加而单调递减的函数
找出这两个函数的交点，在交点处就能保证这两个函数的最大值最小
X的值只能取整数，就是离这两个函数的交点左右两侧最近的整数
如果dp[K-1][X-1]<dp[K][N-X]，那么真正的X在查找到的X的右侧，否则真正的X在查找到的X的左侧
3.转换思路，如果做T次操作，有K个鸡蛋，那么我们能找到答案的最高的楼层N是多少
dp[T][K]为在上述条件下的楼层N，只需要找出最小的满足dp[T][K]>=N的T
要找出最高的楼层N，不必思考在哪里扔这个鸡蛋
只需要扔出一个鸡蛋：鸡蛋碎了，这一层的下方有dp[T-1][K-1]层
鸡蛋不碎，这一层的上方有dp[T-1][K]层
当前层也要加1，总层数dp[T-1][K-1]+dp[T-1][K]+1>=N
上面的我不是太清楚，我的理解：
只需要扔出一个鸡蛋：鸡蛋碎了，这一层的下方有dp[T-1][K-1]层，上方N-X层被验证（都会碎）
当前层也要加1，总层数dp[T-1][K-1]+N-X+1
鸡蛋不碎，这一层的上方有dp[T-1][K]层，下方X-1层被验证（都不碎）
当前层也要加1，总层数dp[T-1][K]+X-1+1
鸡蛋碎和不碎概率50%
两种情况总层数相加除以2
dp[T-1][K-1]+N-X+1+dp[T-1][K]+X-1+1=dp[T-1][K-1]+N+dp[T-1][K]+1
(dp[T-1][K-1]+N+dp[T-1][K]+1)/2>=N
dp[T-1][K-1]+N+dp[T-1][K]+1>=2N
dp[T-1][K-1]+dp[T-1][K]+1>=N
'''

K = 2
N = 100
dp = np.zeros([K + 1, N + 1])
for i in range(1, K + 1):
    dp[i, 1] = 1
for j in range(1, N + 1):
    dp[1, j] = j

for i in range(2, K + 1):
    for j in range(2, N + 1):
        min_value = 10000
        for k in range(1, j + 1):
            min_value = min(min_value, max(dp[i - 1, k - 1], dp[i, j - k]))
        dp[i, j] = min_value + 1

print(dp[K, N])

K = 2
N = 100
dp = np.zeros([K + 1, N + 1])
for i in range(1, K + 1):
    dp[i, 1] = 1
for j in range(1, N + 1):
    dp[1, j] = j

for i in range(2, K + 1):
    for j in range(2, N + 1):
        lo = 1
        hi = j
        while lo + 1 < hi:
            k = (lo + hi) // 2
            if dp[i - 1, k - 1] < dp[i, j - k]:
                lo = k
            elif dp[i - 1, k - 1] > dp[i, j - k]:
                hi = k
            else:
                lo = hi = k
        dp[i, j] = min(max(dp[i - 1, lo - 1], dp[i, j - lo]), max(dp[i - 1, hi - 1], dp[i, j - hi])) + 1

print(dp[K, N])

K = 2
N = 100
dp = np.zeros([N + 1, K + 1])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        dp[i, j] = dp[i - 1, j - 1] + dp[i - 1, j] + 1
    if dp[i, K] >= N:
        result = i
        print(result)
        break
