'''
在 MOE 模型训练时，token 会依据概率发送到 topk 个不同专家计算，这些专家分布在多个 NPU 卡上。
Device-Limited routing 算法可将 token 路由目标限制在p个 NPU 以降低通信成本，具体步骤如下：
 - 把 n 个专家平均分配在 m 个 NPU 上，每个 NPU 上的专家为一个组；设n个专家的编号为 N=[0,1,2,...,n-1]，
   同一个专家组上的专家编号是连续的；
 - 每个专家对应一个概率，表示被路由到的可能性；用每个组中的最大概率作为本组代表，从所有组中选择概率最大的 p 个组，
   其所在的NPU即为路由目标限制 NPU;
 - 再从上述 p 个 NPU 对应的所有专家概率中选择k个最大的概率对应的专家编号作为最终路由目标。

试编写一段程序，实现以上路由算法。

输入描述
 - 第一行有4个处于区间[1,10000]之内的整数，
   第1个表示专家的个数n，第2个表示NPU个数m，第3个表示路由目标限制 NPU 数 p，第4个表示目标路由专家个数 k;
 - 第二行有n个处于区间（0,1）之内的浮点数，表示每个专家对应的概率值，这n个数对应的专家的编号为[0,1,2,...,n-1]。

输出描述
 - 如果 n 不能被 m 整除或者获取不到k个专家编号，输出error；
 - 否则，按照从小到大的顺序，输出k个专家编号，任意相邻两数之间有空格，最后一个数字 (行尾没有空格)。
'''

DEBUG_MODE = False

if DEBUG_MODE:
    import sys
    import json
    from io import StringIO
    with open("questions/q_3.json", 'r') as f:
        obj = json.load(f)
        st = obj['main'][1]['i']
        sys.stdin = StringIO('\n'.join(st))

N, M, P, K = map(int, input().split())

if (N % M):
    print("error")
    exit()

group_size = N // M

idces = list(range(N)) # experts id
probs = list(map(float, input().split())) # expert probs

probs_group = [max(probs[group_size * m:group_size * (m + 1)]) for m in range(M)]
groups = list(range(M))
groups.sort(key=lambda x:probs_group[x], reverse=True)

selected_group = groups[:P]
selected_experts = []
for g in selected_group:
    selected_experts.extend(idces[group_size * g:group_size * (g + 1)])  # all exports in selected groups
selected_experts.sort(key=lambda x:probs[x], reverse=True)  # reorder the experts by probs

if (len(selected_experts) < K):
    print("error")
    exit()

selected_experts = selected_experts[:K]  # top-k expert
selected_experts.sort()  # reorder the experts by ids

print(' '.join([str(e) for e in selected_experts]))