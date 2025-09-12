import math

def info_entropy(posi: list) -> float:
    h = 0
    for p in posi:
        assert p > 0, f"Expect possibility larger than 0, got {p}."
        h -= p * math.log2(p)
    return h

def info_entropy_of_count(count: dict, total: int) -> float:
    s_total = sum(count.values())
    assert total > 0, f"Expect total amout larger than 0, got {total}."
    return info_entropy([amount / s_total for amount in count.values() if amount > 0]) * (s_total / total)

def build_tree(tree: list, idx: int, data: list, select: list, feats: list, count: dict, entropy_th: float = 0.5):
    # Leaf
    entropy = info_entropy_of_count(count, len(select))
    if ((entropy < entropy_th) or
        (len(feats) == 0)): # Leaf
        tree[idx - 1] = [0, 0, -1, -1, max(count, key=count.get)]
        return
        
    # Non-Leaf (Maybe)
    entropy_record = math.inf
    l_count_rec = 0
    r_count_rec = 0
    feat_record = 0
    split_record = 0

    # Traverse features
    for feat in feats:
        # Traverse datas
        select.sort(key=lambda x:data[x][feat])
        l_count = {}
        r_count = count.copy()  # init primary split
        for i in range(len(select) - 1):
            s, s_ = select[i], select[i + 1]
            l_count[data[s][-1]] = l_count.get(data[s][-1], 0) + 1  # shift to left
            r_count[data[s][-1]] -= 1  # remove from right

            # Find Middle Point
            if (data[s][feat] == data[s_][feat]):
                continue
            l_h, r_h = info_entropy_of_count(l_count, len(select)), info_entropy_of_count(r_count, len(select))
            if l_h + r_h < entropy_record:
                entropy_record = l_h + r_h
                l_count_rec, r_count_rec = l_count.copy(), r_count.copy()  # record frequency
                feat_record, split_record = feat, (data[s][feat] + data[s_][feat]) / 2

    # Might Still Leaf...
    if (entropy < entropy_record):
        tree[idx - 1] = [0, 0, -1, -1, max(count, key=count.get)]
        return

    # Not-Leaf (For Sure)
    # Split data
    l_select = [s for s in select if data[s][feat_record] <= split_record]
    r_select = [s for s in select if data[s][feat_record] >  split_record]
    remain_feats = feats.copy()
    remain_feats.remove(feat_record)

    # Make Node
    tree.append([])
    l_idx = len(tree)
    build_tree(tree, l_idx, data, l_select, remain_feats, l_count_rec, entropy_th)
    
    tree.append([])
    r_idx = len(tree)
    build_tree(tree, r_idx, data, r_select, remain_feats, r_count_rec, entropy_th)

    tree[idx - 1] = [l_idx, r_idx, feat_record, split_record, max(count, key=count.get)]

def is_leaf(node: list) -> bool:
    return node[0] == 0 and node[1] == 0

def infer_tree(tree: list, data: list) -> int:
    node = tree[0]
    while not is_leaf(node):
        if (data[node[2]] <= node[3]):
            node = tree[node[0] - 1]
        else:
            node = tree[node[1] - 1]
    return int(node[-1])

def test_tree(tree: list, datas: list) -> float:
    correct = 0
    for data in datas:
        label = data[-1]
        infer = infer_tree(tree, data[:-1])
        correct += label == infer
    print(f"Acc: {correct / len(datas) * 100.0:.6f}%, {correct}/{len(datas)}")

from dataset import *
dataset = generate_fruit_dataset
# dataset = generate_three_body_dataset
# dataset = impossible_dataset
# dataset = challenging_set
# dataset = heart_attack_set
# dataset = fruits_set

datas = dataset(200, 0)

tree = [[]]
count = {}
for data in datas:
    count[data[-1]] = count.get(data[-1], 0) + 1
select = list(range(len(datas)))
feats = list(range(len(datas[0]) - 1))
build_tree(tree, 1, datas, select, feats, count, entropy_th=0.2)
print(tree)

test_datas = dataset()
test_tree(tree, test_datas)

with open("./txt.txt", 'w+') as f:
    [f.write(f'"{",".join([str(n) for n in line])}"\n') for line in tree]
    [f.write(f'"{",".join([str(n) for n in line])}"\n') for line in test_datas]