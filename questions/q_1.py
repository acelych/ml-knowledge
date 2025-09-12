'''
KNN 算法的核心思想是，如果一个样本在特征空间中的 K 个最相邻的样本中的大多数属于某一个类别，
则该样本也属于这个类别，并具有这个类别上样本的特性。请按照如下步骤，实现 KNN 算法。

KNN算法说明：
计算待分类点到其他样本点的距离；
通过距离进行排序，选择距离最小的K个点；提取这K个临近点的类别，根据少数服从多数的原则，将占比最多的那
个标签赋值给待分类样本点的label。
本题说明：
1、给定数据集中，默认每一类标签都存在数据，不存在某类型数量为0的场景；
2、为消除不同特征权重问题，给出数据均已做好归一化处理，并保留两位小数；
3、出现并列第一的情形时，取并列第一的样本中，最近邻居的标签返回；
4、距离函数定义为: $d_{x,y}=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}$

输入描述
第1行：$k,m,n,s$：k代表每次计算时选取的最近邻居个数（不大于20），m代表样本数量(不大于200），n代表样本
维度（不包括标签，不大于5)，s代表类别个数（不小于5);
第2行：待分类样本
第3行~第 $m+2$ 行：m个样本，每一行n+1列，最后一列为类别标签 label
'''

import math

def calc_distance(la: list, lb: list) -> float:
    assert len(la) == len(lb)
    return math.sqrt(sum([(la[i] - lb[i]) ** 2 for i in range(len(la))]))

# 读取第一行输入：k（最近邻数量），m（样本数量），n（特征维度），s（类别数量）
k, m, n, s = map(int, input().split())

# 读取待分类样本的特征向量
target = list(map(float, input().split()))

# 读取所有训练样本
samples = []
for _ in range(m):
    sample = list(map(float, input().split()))
    samples.append(sample)

# 存储所有样本到待分类样本的距离及其标签
distances = []

# 遍历所有样本，并计算当前样本到待分类样本的距离并存储（距离值，标签）
for sample in samples:
    distances.append((calc_distance(target, sample[:-1]), sample[-1]))

# 按距离从小到大排序，并取前k个最近邻
distances = sorted(distances, key=lambda x:x[0])[:k]
distances_count = {}
distances_close = {}
for distance in distances:
    # 如果该标签还未出现过，记录其最近的距离值
    if distance[1] not in distances_count:
        distances_close[distance[1]] = distance[0]
    # 统计每个标签出现的次数
    distances_count[distance[1]] = distances_count.get(distance[1], 0) + 1
# 按出现次数从大到小排序，出现次数相同的按最近距离排序
distances_count = sorted(distances_count.items(), key=lambda x:x[1], reverse=True)

# 取出出现次数最多的标签，如果出现并列第一的情形时，取并列第一的样本中，最近邻居的标签返回
max_num = distances_count[0][1]
distances_count = [(k, v) for k, v in distances_count if v == max_num]
distances_count = sorted(distances_count, key=lambda x:distances_close[x[0]])

print(int(distances_count[0][0]))