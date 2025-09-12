'''
在云存储系统中，需预测存储设备故障以提前迁移数据。每条设备日志包含：设备ID, 写入次数，读取次数，平均写入延迟(ms), 
平均读取延迟 (ms)，设备使用年限(年)，设备状态 (0 正常/1故障)。需实现一个设备故障预测系统，包含以下功能：
1. 数据清洗：
    - 写入/读取次数：<0;
    - 平均写入/读取延迟：<0或>1000;
    - 使用年限：<0或>20。异常值用该字段有效值的中位数替换。
    - 缺失值标记为"NaN"，用该字段有效值的均值填充。
2. 逻辑回归模型：
    - 使用批量梯度下降法(Batch GD)训练，每次迭代使用全部样本。
    - 特征：[写入次数，读取次数，平均写入延迟，平均读取延迟，设备使用年限]。
    - 标签：设备状态。
    - 参数：迭代100次，学习率α=0.01，初始权重全为 0。
3.预测输出：
    - 预测结果：0(正常）或1(故障)。

输入描述
    - 第一行为训练总个数N，(2<=N<=100)。
    - 第二行起连续N行训练数据，每个训练数据包含：设备ID，写入次数，读取次数，平均写入延迟，平均读取延迟，设备使用年限，状态。
    - 第N+2行为预测数据总个数M，（1<=M<=10)
    - 第N+3行起连续M行预测数据，每个预测数据包含：设备ID，写入次数，读取次数，平均写入延迟，平均读取延迟，设备使用年限。
输出描述
    - 输出M行预测结果。
'''

DEBUG_MODE = True

if DEBUG_MODE:
    import sys
    import json
    from io import StringIO
    with open("questions/q_4.json", 'r') as f:
        obj = json.load(f)
        st = obj['main'][1]['i']
        sys.stdin = StringIO('\n'.join(st))
N = int(input())

train_datas = []
for _ in range(N):
    train_datas.append(input().split())

M = int(input())

predict_datas = []
for _ in range(M):
    predict_datas.append(list(map(float, input().split())))

# wash data
it_sum, ot_sum, aid_sum, aod_sum, year_sum = [], [], [], [], []
for data in train_datas:
    data[1] = "NaN" if (data[1] == "NaN" or float(data[1]) < 0) else float(data[1])
    data[2] = "NaN" if (data[2] == "NaN" or float(data[2]) < 0) else float(data[2])
    data[3] = "NaN" if (data[3] == "NaN" or float(data[3]) < 0 or float(data[3]) > 1000) else float(data[3])
    data[4] = "NaN" if (data[4] == "NaN" or float(data[4]) < 0 or float(data[4]) > 1000) else float(data[4])
    data[5] = "NaN" if (data[5] == "NaN" or float(data[5]) < 0 or float(data[5]) > 20) else float(data[5])
    data[6] = float(data[6])
    if isinstance(data[1], float):
        it_sum.append(data[1])
    if isinstance(data[2], float):
        ot_sum.append(data[2])
    if isinstance(data[3], float):
        aid_sum.append(data[3])
    if isinstance(data[4], float):
        aod_sum.append(data[4])
    if isinstance(data[5], float):
        year_sum.append(data[5])

it = sum(it_sum)/len(it_sum)
ot = sum(ot_sum)/len(ot_sum)
aid = sum(aid_sum)/len(aid_sum)
aod = sum(aod_sum)/len(aod_sum)
year = sum(year_sum)/len(year_sum)
    
for i, data in enumerate(train_datas):
    if isinstance(data[1], str):
        data[1] = it
    if isinstance(data[2], str):
        data[2] = ot
    if isinstance(data[3], str):
        data[3] = aid
    if isinstance(data[4], str):
        data[4] = aod
    if isinstance(data[5], str):
        data[5] = year

# normalize
def normalize(datas: list, dims_max_min: list = None):
    dims = len(datas[0])
    if dims_max_min is None:
        dims_max_min = []
        record = True
    else:
        record = False
    for dim in range(dims):
        if record:
            max_v = max([data[dim] for data in datas])
            min_v = min([data[dim] for data in datas])
            dims_max_min.append((max_v, min_v))
        else:
            max_v, min_v = dims_max_min[dim]
        for data in datas:
            data[dim] = (data[dim] - min_v) / (max_v - min_v)
    return dims_max_min

# logic regression
import math

weight = [0.0 for _ in range(len(train_datas[0]) - 2)]
bias = 0.0
learn_rate = 0.05

def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))

def diff_sigmoid(y: float):
    return y * (1 - y)

def diff_mse(pred: list, label: list) -> list:
    return list([(p - l) * 2 / len(pred) for (p, l) in zip(pred, label)])

def diff_bce_sigmoid(pred: list, label: list) -> list:
    return list([y_p - y for (y_p, y) in zip(pred, label)])

def forward_and_backward(x: list, label: list):
    global weight, bias

    # forward
    y_mat = [sum([xn * wn for (xn, wn) in zip(x_batch, weight)]) + bias for x_batch in x]
    y_sig = [sigmoid(yn) for yn in y_mat]
    # loss
    # grad_m = diff_mse(y_sig, label)
    grad_m = [1.0 for _ in range(len(y_sig))]
    # backward
    # grad_s = [diff_sigmoid(yn) for yn in y_sig]
    grad_s = diff_bce_sigmoid(y_sig, label)  # grad (bce multi sig)
    grad_w = [[x[ib][iw] for ib in range(len(x))] for iw in range(len(weight))]
    grad_b = 1
    # step
    grad_W = [sum([gw * gs * gm for (gw, gs, gm) in zip(gwi, grad_s, grad_m)])/len(x) for gwi in grad_w]
    grad_B = sum([grad_b * gs * gm for (gs, gm) in zip(grad_s, grad_m)])/len(x)
    weight = [w - learn_rate * gW for (w, gW) in zip(weight, grad_W)]
    bias -= learn_rate * grad_B

def forward(x: list):
    y_mat = [sum([xn * wn for (xn, wn) in zip(x_batch, weight)]) + bias for x_batch in x]
    y_sig = [sigmoid(yn) for yn in y_mat]
    return [int(yn > 0.5) for yn in y_sig]

# train
epochs = 100
x = [data[1:-1] for data in train_datas]
label = [data[-1] for data in train_datas]
dims_max_min = normalize(x)

for epoch in range(epochs):
    forward_and_backward(x, label)
    pred = forward(x)
    acc = sum([p == l for (p, l) in zip(pred, label)]) / len(label)
    print(f"epoch: {epoch}, acc: {acc}")

# predict
x = [data[1:] for data in predict_datas]
normalize(x, dims_max_min)

pred = [str(p) for p in forward(x)]
print(' '.join(pred))