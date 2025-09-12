'''
决策树生成算法递归地产生决策树，直到不能继续下去为止，这样产生的树往往对训练数据的分类很准确，但对未知的
测试数据的分类却没有那么准确，即出现过拟合现象。
在决策树学习中将已生成的树进行简化的过程称为剪枝。具体地，剪枝从已生成的树上裁掉一些子树或叶节点，并将其
根节点或父节点作为新的叶节点，从而简化分类树模型。
小A希望通过决策树的方法解决一个二分类任务。在该二分类的任务中，标签 1 是正分类，标签 0 是负分类。现在小A
已经训练了一个未剪枝的二分类的决策树。他希望对该决策树进行剪枝，能够在验证集上达到最优的F1值。
给定一个二叉树为待剪枝的二分类决策树，每个节点有 3 个参数f_i、th_i;、label_i;。当节点非叶节点时，f_i、th_i; 表示
该节点决策应用的特征编号和阀值。在数据的第f_i个特征小于等于th_i时决策走左节点，大于th_i时走右节点。决策
树的预测通过该规则推理到叶节点时，叶节点的label_i为该条数据的预测结果。
请输出小A通过剪枝在验证集上可以达到的最优 F1 值。

输入描述
第一行为一个N、M、K。其中，N(1<= N <= 100）表示决策树的节点个数。
M (1 <= M <= 300) 表示的验证集条数。
K (1 <= K <= 100) 表示每条验证集特征个数。
随后 N 行，第 i 行表示第 i 个节点，根节点编号为 1，每行包括 5 个整数l_i、r_i、f_i、th_i;、label_i;。其中l_i、r_i分别表，
示节点的左右子节点编号(0<=l_ir_i<= 100）。若 l_i=0、r_i=0 则表示无子节点，不存在只有一个子节点的情况。
当节点非叶节点时，f_i、th_i，表示该节点的特征编号和阔值，否则 f_i、th_i为0。label_i表示当该节点作为叶节点
时的分类结果(label_i 取值为 0 或 1）
随后 M 行为验证集特征和 label，每行 K+1 个整数，前 K 个整数为该条数据的特征，最后一个整数位该条数据的label。
'''

DEBUG_MODE = True

if DEBUG_MODE:
    import sys
    import json
    from io import StringIO
    with open("questions/q_2.json", 'r') as f:
        obj = json.load(f)
        st = obj['main'][0]['i']
        sys.stdin = StringIO('\n'.join(st))

def is_leaf(node: list) -> bool:
    return node[0] == 0 and node[1] == 0

def infer_tree(tree: list, data: list) -> int:
    node = tree[0]
    while not is_leaf(node):
        if (data[int(node[2])] <= node[3]):
            node = tree[int(node[0] - 1)]
        else:
            node = tree[int(node[1] - 1)]
    return int(node[-1])

def calc_f1(tree: list, datas: list) -> float:
    tp = 0
    fp = 0
    fn = 0
    for data in datas:
        label = int(data[-1])
        infer = infer_tree(tree, data[:-1])
        if label == 1 and infer == 1:
            tp += 1
        elif label == 1 and infer == 0:
            fn += 1
        elif label == 0 and infer == 1:
            fp += 1
    precision = tp / (tp + fp + 1e-9)
    recall = tp / (tp + fn + 1e-9)
    return (2 * precision * recall) / (precision + recall + 1e-9)

def calc_acc(tree: list, datas: list) -> float:
    correct = 0
    for data in datas:
        label = data[-1]
        infer = infer_tree(tree, data[:-1])
        correct += label == infer
    return correct / len(datas)

N, M, K = map(int, input().split())

tree = []
for _ in range(N):
    tree.append(list(map(float, input().split())))

datas = []
for _ in range(M): 
    datas.append(list(map(float, input().split())))

orig_f1 = calc_f1(tree, datas)
orig_acc = calc_acc(tree, datas)

def dbfs_prune(tree: list, datas: list, nodes: list):
    global best_f1, best_acc, ct

    nodes = [node for node in nodes if not is_leaf(tree[node-1])]
    if (len(nodes) == 0):
        return

    for i in range(1 << len(nodes)):  # traverse 0 to 2^n - 1
        pile1 = []  # not prune
        pile2 = []  # prune
        for j in range(len(nodes)):
            if (i >> j) & 1:  # check if the j bit is 1
                pile1.append(nodes[j])
            else:
                pile2.append(nodes[j])
        # save state
        lr_states = []
        for n in pile2:
            lr_states.append(tuple(map(int, tree[n-1][:2])))
            tree[n-1][:2] = 0, 0
        lr_recurs = []
        # test 
        f1, acc = calc_f1(tree, datas), calc_acc(tree, datas)
        best_f1, best_acc = max(f1, best_f1), max(acc, best_acc)
        # do recursion
        for n in pile1:
            if is_leaf(tree[n-1][:2]):
                continue  # leaf node
            lr_recurs.extend(map(int, tree[n-1][:2]))  # recursion for non-leaf node
        dbfs_prune(tree, datas, lr_recurs)
        # recover state
        for (n, lr_state) in zip(pile2, lr_states):
            tree[n-1][:2] = lr_state

def dfs_prune(tree: list, datas: list, idx: int):

    if (is_leaf(tree[idx-1])):
        return

    l, r = map(int, tree[idx-1][:2])
    tree[idx-1][:2] = 0, 0
    f1_prune = calc_f1(tree, datas)
    tree[idx-1][:2] = l, r

    dfs_prune(tree, datas, l)
    dfs_prune(tree, datas, r)

    f1_not_prune = calc_f1(tree, datas)
    if f1_prune > f1_not_prune:
        tree[idx-1][:2] = 0, 0

dfs_prune(tree, datas, 1)

best_f1 = calc_f1(tree, datas)
best_acc = calc_acc(tree, datas)

# print(f"original f1 score: {orig_f1}, acc: {orig_acc}; best f1 score: {best_f1}, acc: {best_acc}")
print(best_f1)

