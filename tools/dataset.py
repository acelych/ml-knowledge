def apple_set() -> list:
    # # 特征矩阵 X (shape: 15行 x 4列)
    X = [
        [0, 150, 0, 8],  # 样本1
        [1, 170, 0, 7],  # 样本2
        [2, 130, 0, 6],  # 样本3
        [0, 160, 0, 9],  # 样本4
        [1, 120, 0, 5],  # 样本5
        [3, 200, 1, 3],  # 样本6
        [2, 180, 1, 2],  # 样本7
        [3, 150, 1, 4],  # 样本8
        [1, 140, 1, 6],  # 样本9
        [0, 120, 1, 7],  # 样本10
        [2, 100, 0, 4],  # 样本11
        [0, 180, 0, 8],  # 样本12
        [3, 220, 1, 2],  # 样本13
        [1, 130, 0, 5],  # 样本14
        [2, 150, 1, 3]   # 样本15
    ]

    # 目标向量 y (shape: 15个元素)
    y = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    datas = list([x + i for x, i in zip(X, [[y[i]] for i in range(len(y))])])
    return datas

def fruits_set() -> list:
    datas = [
        # 特征: [R, G, B, 重量(g), 直径(cm), 纹理, 产地, 是否有斑点/条纹, 标签]
        [255, 0, 0, 150, 7.5, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 120, 18.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 180, 8.0, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 160, 7.0, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 170, 8.2, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 130, 19.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 160, 7.8, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 140, 6.5, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 145, 7.0, '轻微粗糙', '温带', '否', '苹果'],  # 纹理略有不同
        [255, 255, 0, 125, 17.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 175, 8.5, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 155, 7.2, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 165, 7.8, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 110, 20.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 190, 8.2, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 170, 7.5, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 155, 7.3, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 140, 18.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 170, 7.9, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 150, 6.8, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 160, 7.6, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 115, 19.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 185, 8.3, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 165, 7.1, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 175, 8.0, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 135, 17.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 155, 7.7, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 145, 6.9, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 148, 7.4, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 122, 18.2, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 168, 8.1, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 158, 7.3, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 162, 7.7, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 128, 19.2, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 172, 7.6, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 152, 6.7, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 168, 7.9, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 117, 20.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 178, 8.4, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 163, 7.4, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 152, 7.2, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 142, 18.8, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 165, 7.5, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 147, 6.6, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 158, 7.8, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 108, 21.0, '光滑', '热带', '否', '香蕉'], # 特别长的香蕉
        [255, 165, 0, 182, 8.6, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 172, 7.6, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 172, 8.1, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 132, 17.2, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 188, 8.0, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 138, 7.0, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 142, 7.1, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 137, 18.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 162, 7.4, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 167, 7.7, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 166, 7.5, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 113, 19.8, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 174, 8.2, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 157, 6.5, '光滑', '温带', '是', '梨'], # 较小的梨
        [255, 0, 0, 153, 7.0, '轻微粗糙', '温带', '否', '苹果'], # 纹理略有不同
        [255, 255, 0, 127, 18.7, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 176, 7.8, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 161, 7.1, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 159, 7.4, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 119, 20.2, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 180, 8.1, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 154, 6.8, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 164, 7.9, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 124, 17.8, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 164, 7.3, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 169, 7.8, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 149, 7.3, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 136, 19.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 186, 8.5, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 143, 6.9, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 171, 8.0, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 129, 18.3, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 158, 7.6, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 156, 7.2, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 157, 7.5, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 118, 20.8, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 192, 8.7, '轻微粗糙', '亚热带', '否', '橙子'], # 较大的橙子
        [0, 255, 0, 162, 7.9, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 146, 7.2, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 123, 17.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 166, 7.7, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 148, 6.4, '光滑', '温带', '是', '梨'], # 较小的梨
        [255, 0, 0, 163, 7.6, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 134, 19.0, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 170, 8.0, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 159, 7.5, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 169, 8.1, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 105, 22.0, '光滑', '热带', '否', '香蕉'], # 非常长的香蕉
        [255, 165, 0, 184, 8.3, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 164, 7.3, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 151, 7.1, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 141, 18.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 160, 7.2, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 153, 6.7, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 167, 7.8, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 131, 17.7, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 178, 8.4, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 168, 7.4, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 154, 7.0, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 126, 20.5, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 182, 7.9, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 146, 6.6, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 161, 7.7, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 114, 19.3, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 174, 8.1, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 155, 7.0, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 176, 8.2, '光滑', '温带', '否', '苹果'],
        [255, 255, 0, 139, 17.3, '光滑', '热带', '否', '香蕉'],
        [255, 165, 0, 188, 8.5, '轻微粗糙', '亚热带', '否', '橙子'],
        [0, 255, 0, 160, 7.6, '光滑', '温带', '是', '梨'],
        [255, 0, 0, 150, 7.3, '光滑', '温带', '否', '苹果'], # 最后一条
    ]

    texture = ["光滑", "轻微粗糙", "非常粗糙", "有绒毛"]
    origin = ["热带", "温带", "亚热带"]
    striped = ["是", "否"]
    label = ["苹果", "香蕉", "橙子", "梨"]
    datas = [data[:5] + [texture.index(data[5]), origin.index(data[6]), striped.index(data[7]), label.index(data[8])] for data in datas]
    return datas

def heart_attack_set() -> list:
    datas = [
        # [age, resting_bp, cholesterol, max_hr, st_depression, chest_pain_type, exercise_angina, oldpeak, slope, ca, label]
        [57, 140, 241, 150, 1.2, 1, 0, 1.4, 1, 0, 0],
        [45, 120, 225, 148, 0.0, 3, 0, 0.0, 2, 0, 0],
        [63, 145, 233, 132, 2.3, 2, 1, 2.1, 0, 2, 1],
        [52, 138, 196, 169, 0.8, 0, 0, 0.8, 2, 0, 0],
        [68, 180, 294, 110, 4.1, 1, 1, 3.8, 0, 3, 1],
        [49, 130, 204, 156, 0.2, 3, 0, 0.1, 2, 0, 0],
        [71, 160, 286, 108, 3.9, 2, 1, 3.5, 0, 2, 1],
        [37, 110, 211, 170, 0.0, 0, 0, 0.0, 2, 0, 0],
        [54, 150, 195, 126, 1.8, 1, 1, 1.7, 1, 1, 1],  # 关键边界点
        [62, 140, 268, 130, 2.8, 2, 1, 2.6, 0, 1, 1],
        [43, 122, 213, 165, 0.1, 3, 0, 0.0, 2, 0, 0],
        [66, 152, 277, 112, 3.2, 1, 1, 3.0, 0, 2, 1],
        [58, 136, 229, 142, 1.5, 0, 0, 1.3, 1, 0, 0],
        [50, 142, 218, 158, 0.6, 3, 0, 0.5, 2, 0, 0],
        [74, 170, 309, 100, 4.5, 2, 1, 4.2, 0, 3, 1],
        [41, 118, 197, 172, 0.0, 0, 0, 0.0, 2, 0, 0],
        [55, 144, 245, 135, 2.1, 1, 1, 1.9, 0, 1, 1],
        [60, 155, 260, 120, 3.0, 2, 1, 2.8, 0, 2, 1],
        [47, 128, 234, 152, 0.9, 3, 0, 0.7, 1, 0, 0],
        [69, 162, 291, 105, 4.0, 1, 1, 3.7, 0, 3, 1],
        # ---------------------------------- 噪声数据开始 ----------------------------------
        [35, 190, 180, 190, 0.0, 0, 0, 0.0, 2, 0, 1],  # 矛盾数据：年轻+高血压但标签为患病
        [80, 100, 400, 90, 5.0, 3, 0, 5.0, 2, 0, 0],   # 矛盾数据：老年+高危特征但标签健康
        # ---------------------------------- 复杂决策边界区域 ----------------------------------
        [53, 142, 238, 138, 1.6, 1, 0, 1.5, 1, 0, 0],  # age*st_depression=84.8 < 阈值
        [54, 143, 240, 137, 1.7, 1, 0, 1.6, 1, 0, 1],  # age*st_depression=91.8 > 阈值 (关键转折点)
        [61, 148, 255, 128, 2.5, 2, 1, 2.3, 0, 1, 1],  # (cholesterol/50) + oldpeak > 7.0
        [59, 146, 248, 130, 2.2, 2, 1, 2.0, 0, 1, 1],  # 同上
        [65, 154, 272, 115, 3.1, 1, 1, 2.9, 0, 2, 1],  # 线性组合: 0.1*age + 0.5*st_depression > 2.0
        # 生成更多数据点（省略详细列出，包含以下特性）：
        # 1. 年龄>65且st_depression>2.0的样本80%患病
        # 2. max_hr < 120且exercise_angina=1的样本75%患病
        # 3. 胆固醇>250且ca>1的样本90%患病
        # 4. 随机插入10%的噪声点（标签翻转）
        # 5. 在决策边界附近密集采样（如st_depression=1.5-2.0区间）
        # 6. 添加5个完全随机的冗余特征值
        # ...（共200条数据）...
        [72, 175, 301, 98, 4.3, 2, 1, 4.0, 0, 3, 1],
        [44, 126, 207, 160, 0.3, 3, 0, 0.2, 2, 0, 0],
        [51, 139, 227, 144, 1.3, 0, 0, 1.1, 1, 0, 0]   # 最后一条
    ]

    import random

    # 生成更多边界点 (规则5)
    for _ in range(40):  # 在st_depression=1.5-2.0区间密集采样
        age = random.randint(45, 65)
        st_depression = random.uniform(1.5, 2.0)
        # 核心规则: age * st_depression > 90 → 患病
        label = 1 if age * st_depression > 90 else 0
        
        # 添加噪声 (规则4)
        if random.random() < 0.1:  # 10%概率翻转标签
            label = 1 - label
        
        datas.append([
            age,
            random.randint(110, 180),
            random.randint(180, 300),
            random.randint(110, 160),
            st_depression,
            random.choice([0, 1, 2, 3]),
            random.choice([0, 1]),
            round(st_depression - random.uniform(0.1, 0.3), 1),
            random.choice([0, 1, 2]),
            random.randint(0, 3),
            label
        ])

    # 规则1: 年龄>65且st_depression>2.0的样本80%患病
    for _ in range(30):
        age = random.randint(66, 80)
        st_depression = random.uniform(2.1, 4.0)
        # 80%患病
        label = 1 if random.random() < 0.8 else 0
        
        # 添加噪声 (规则4)
        if random.random() < 0.1:
            label = 1 - label
        
        datas.append([
            age,
            random.randint(130, 200),
            random.randint(200, 380),
            random.randint(80, 130),
            st_depression,
            random.choice([0, 1, 2]),
            random.choice([0, 1]),
            round(st_depression - random.uniform(0.1, 0.5), 1),
            random.choice([0, 1]),
            random.randint(0, 3),
            label
        ])

    # 规则2: max_hr < 120且exercise_angina=1的样本75%患病
    for _ in range(25):
        max_hr = random.randint(70, 119)
        # 75%患病
        label = 1 if random.random() < 0.75 else 0
        
        # 添加噪声 (规则4)
        if random.random() < 0.1:
            label = 1 - label
        
        datas.append([
            random.randint(40, 75),
            random.randint(100, 180),
            random.randint(180, 350),
            max_hr,
            random.uniform(0.5, 3.5),
            random.choice([1, 2]),
            1,  # exercise_angina=1
            random.uniform(0.5, 3.0),
            random.choice([0, 1]),
            random.randint(0, 3),
            label
        ])

    # 规则3: 胆固醇>250且ca>1的样本90%患病
    for _ in range(35):
        cholesterol = random.randint(251, 380)
        ca = random.choice([2, 3])
        # 90%患病
        label = 1 if random.random() < 0.9 else 0
        
        # 添加噪声 (规则4)
        if random.random() < 0.1:
            label = 1 - label
        
        datas.append([
            random.randint(50, 75),
            random.randint(120, 190),
            cholesterol,
            random.randint(90, 150),
            random.uniform(1.0, 4.0),
            random.choice([1, 2]),
            random.choice([0, 1]),
            random.uniform(1.0, 3.5),
            random.choice([0, 1]),
            ca,
            label
        ])

    # 生成剩余数据 (规则6: 添加随机冗余特征值)
    for _ in range(50):  # 200 - 20 - 40 - 30 - 25 - 35 = 50
        # 随机生成特征
        age = random.randint(30, 80)
        resting_bp = random.randint(90, 200)
        cholesterol = random.randint(100, 400)
        max_hr = random.randint(60, 200)
        st_depression = random.uniform(0.0, 6.0)
        chest_pain_type = random.choice([0, 1, 2, 3])
        exercise_angina = random.choice([0, 1])
        oldpeak = random.uniform(0.0, 6.0)
        slope = random.choice([0, 1, 2])
        ca = random.randint(0, 3)
        
        # 核心规则决定标签
        if (age * st_depression > 90) or \
        (cholesterol/50 + oldpeak > 7) or \
        (0.1*age + 0.5*st_depression > 2.0 and ca >= 2):
            label = 1
        else:
            label = 0
        
        # 添加噪声 (规则4)
        if random.random() < 0.1:
            label = 1 - label
        
        datas.append([
            age,
            resting_bp,
            cholesterol,
            max_hr,
            st_depression,
            chest_pain_type,
            exercise_angina,
            oldpeak,
            slope,
            ca,
            label
        ])

    # 确保总数为200条
    datas = datas[:200]

    return datas

import random
import numpy as np
import math
from datetime import datetime, timedelta

def challenging_set(num_samples=1000):
    """
    生成一个极具挑战性的数据集，包含30个特征和1个标签
    返回格式: [[特征1, 特征2, ..., 特征30, 标签], ...]
    """
    np.random.seed(42)  # 固定随机种子以确保可复现性
    data = []
    
    # 基础时间点
    base_date = datetime(2023, 1, 1)
    
    for i in range(num_samples):
        # 特征1-5: 基本特征（有线性关系）
        age = np.random.randint(18, 80)
        income = np.random.normal(50000, 20000)
        education = np.random.randint(1, 10)
        experience = max(0, age - 22 - np.random.randint(0, 5))
        family_size = np.random.randint(1, 6)
        
        # 特征6-10: 非线性变换特征
        log_income = np.log(max(1, income))
        age_squared = age ** 2
        income_age_ratio = income / max(1, age)
        education_sqrt = np.sqrt(education)
        family_size_cubed = family_size ** 3
        
        # 特征11-15: 时间序列特征（随时间变化）
        date_offset = base_date + timedelta(days=i)
        day_of_week = date_offset.weekday()
        day_of_year = date_offset.timetuple().tm_yday
        month = date_offset.month
        quarter = (month - 1) // 3 + 1
        is_weekend = 1 if day_of_week >= 5 else 0
        
        # 特征16-20: 周期性和季节性特征
        sin_day = np.sin(2 * np.pi * day_of_year / 365)
        cos_day = np.cos(2 * np.pi * day_of_year / 365)
        sin_month = np.sin(2 * np.pi * month / 12)
        cos_month = np.cos(2 * np.pi * month / 12)
        holiday_effect = 1 if month in [12, 1, 7] else 0  # 假期月份
        
        # 特征21-25: 特征交互项
        age_income = age * income / 1000
        edu_exp = education * experience
        fam_edu = family_size * education
        age_fam = age * family_size
        income_edu = income * education / 1000
        
        # 特征26-30: 随机但具有隐藏模式的特征
        # 这些特征看起来随机，但包含复杂的决策边界
        cyclic_feature = np.sin(i / 10) * np.cos(i / 7)
        fractal_feature = 0.5 * np.sin(3 * i) + 0.3 * np.cos(5 * i) + 0.2 * np.sin(7 * i)
        chaotic_feature = (i % 17) * (i % 23) / 100
        prime_feature = 1 if is_prime(i) else 0
        fib_feature = 1 if is_fibonacci(i) else 0
        
        # 概念漂移：决策边界随时间变化
        time_factor = i / num_samples
        
        # 核心决策规则（非线性、多特征交互）
        # 规则随时间变化（概念漂移）
        rule1 = (age * income * (1 + 0.5 * time_factor)) > (3000000 * (1 + time_factor))
        rule2 = (education * experience * (1 - 0.3 * time_factor)) > (50 * (1 + 0.2 * time_factor))
        rule3 = (family_size * month * (1 + 0.1 * np.sin(time_factor * 10))) > 30
        rule4 = (day_of_year * cyclic_feature) > 100
        rule5 = (chaotic_feature * fractal_feature) > 0.2
        
        # 多模态分布：不同规则适用于不同群体
        if age < 40:
            label = 1 if rule1 or rule4 else 0
        elif age < 60:
            label = 1 if rule2 or rule5 else 0
        else:
            label = 1 if rule3 or (rule1 and rule2) else 0
        
        # 对抗性噪声：10%的样本标签被翻转
        if np.random.random() < 0.1:
            label = 1 - label
        
        # 添加特征噪声：5%的特征被扰动
        features = [
            age, income, education, experience, family_size,
            log_income, age_squared, income_age_ratio, education_sqrt, family_size_cubed,
            day_of_week, day_of_year, month, quarter, is_weekend,
            sin_day, cos_day, sin_month, cos_month, holiday_effect,
            age_income, edu_exp, fam_edu, age_fam, income_edu,
            cyclic_feature, fractal_feature, chaotic_feature, prime_feature, fib_feature
        ]
        
        # 添加特征噪声
        for j in range(len(features)):
            if np.random.random() < 0.05:
                if isinstance(features[j], int):
                    features[j] += np.random.randint(-2, 2)
                else:
                    features[j] *= np.random.uniform(0.9, 1.1)
        
        # 添加标签
        features.append(label)
        data.append(features)
    
    return data

# 辅助函数：判断是否为质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 辅助函数：判断是否为斐波那契数
def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def impossible_dataset(num_samples=1000):
    # 使用混沌系统生成不可预测数据
    # Lorenz吸引子参数
    sigma, rho, beta = 10.0, 28.0, 8.0/3.0
    dt = 0.01
    x, y, z = 0.1, 0.0, 0.0
    
    data = []
    for i in range(num_samples):
        # 更新混沌系统
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt
        
        # 特征：混沌系统的当前状态+历史状态
        features = [
            x, y, z, 
            x*y, y*z, z*x,
            x**2, y**2, z**2,
            math.sin(x*10), math.cos(y*10),
            random.gauss(0, 1)  # 添加随机噪声
        ]
        
        # 不可预测的标签规则（基于混沌系统的未来状态）
        future_steps = 5
        future_x, future_y, future_z = x, y, z
        for _ in range(future_steps):
            dx = sigma * (future_y - future_x)
            dy = future_x * (rho - future_z) - future_y
            dz = future_x * future_y - beta * future_z
            future_x += dx * dt
            future_y += dy * dt
            future_z += dz * dt
        
        # 标签取决于未来状态（模型无法访问的未来信息）
        label = 1 if future_x > 0 else 0
        
        # 添加特征噪声
        for j in range(len(features)):
            if random.random() < 0.1:
                features[j] += random.gauss(0, 0.1)
        
        features.append(label)
        data.append(features)
    
    return data

def generate_three_body_dataset(num_samples=1000):
    """生成基于三体问题的数据集，不使用复杂库，确保高效"""
    np.random.seed(42)
    data = []
    
    # 计数器确保标签平衡
    label_counts = {0: 0, 1: 0}
    target_count = num_samples // 2
    
    while len(data) < num_samples:
        # 1. 生成三个天体的质量 (归一化)
        masses = np.random.uniform(0.5, 2.0, 3)
        
        # 2. 生成初始位置 (在单位球内)
        positions = np.random.uniform(-1, 1, (3, 3))
        for i in range(3):
            norm = np.linalg.norm(positions[i])
            if norm > 1:  # 确保在单位球内
                positions[i] /= norm * 1.1
        
        # 3. 生成初始速度 (与位置正交)
        velocities = np.zeros((3, 3))
        for i in range(3):
            # 随机方向垂直于位置向量
            direction = np.cross(positions[i], np.random.normal(0, 1, 3))
            direction /= np.linalg.norm(direction) + 1e-8
            # 速度大小与距离成反比
            speed = 0.5 / (np.linalg.norm(positions[i]) + 0.1)
            velocities[i] = direction * speed * np.random.uniform(0.8, 1.2)
        
        # 4. 计算系统总能量 (简化版)
        # 动能
        kinetic = 0
        for i in range(3):
            kinetic += 0.5 * masses[i] * np.sum(velocities[i]**2)
        
        # 势能
        potential = 0
        for i in range(3):
            for j in range(i+1, 3):
                r = np.linalg.norm(positions[i] - positions[j])
                potential -= masses[i] * masses[j] / (r + 1e-8)
        
        total_energy = kinetic + potential
        
        # 5. 计算角动量
        angular_momentum = np.zeros(3)
        for i in range(3):
            angular_momentum += masses[i] * np.cross(positions[i], velocities[i])
        angular_momentum_norm = np.linalg.norm(angular_momentum)
        
        # 6. 计算最小距离
        min_distance = min(
            np.linalg.norm(positions[0]-positions[1]),
            np.linalg.norm(positions[0]-positions[2]),
            np.linalg.norm(positions[1]-positions[2])
        )
        
        # 7. 计算最大速度
        max_speed = max(
            np.linalg.norm(velocities[0]),
            np.linalg.norm(velocities[1]),
            np.linalg.norm(velocities[2])
        )
        
        # 8. 定义标签规则 (基于物理启发式规则)
        # 规则1: 总能量 > 0 可能不稳定
        # 规则2: 角动量小可能不稳定
        # 规则3: 最小距离小可能碰撞
        energy_factor = total_energy
        angular_factor = angular_momentum_norm / (np.sum(masses) + 1e-8)
        distance_factor = min_distance
        
        # 复杂决策规则
        if (energy_factor > 0.2 and angular_factor < 0.3) or \
           (distance_factor < 0.2 and max_speed > 0.8) or \
           (energy_factor > 0.5 and distance_factor < 0.3):
            label = 1  # 不稳定
        else:
            label = 0  # 稳定
        
        # 确保标签平衡
        if label_counts[label] < target_count:
            # 特征列表 (共30个特征)
            features = []
            
            # 基本特征 (9个)
            features.extend(masses)
            features.extend(positions.ravel())
            features.extend(velocities.ravel())
            
            # 衍生特征 (21个)
            # 距离相关
            features.append(np.linalg.norm(positions[0]-positions[1]))
            features.append(np.linalg.norm(positions[0]-positions[2]))
            features.append(np.linalg.norm(positions[1]-positions[2]))
            
            # 速度相关
            features.append(np.linalg.norm(velocities[0]))
            features.append(np.linalg.norm(velocities[1]))
            features.append(np.linalg.norm(velocities[2]))
            
            # 能量相关
            features.append(kinetic)
            features.append(potential)
            features.append(total_energy)
            
            # 角动量相关
            features.extend(angular_momentum)
            features.append(angular_momentum_norm)
            
            # 质心位置
            center_of_mass = np.zeros(3)
            total_mass = np.sum(masses)
            for i in range(3):
                center_of_mass += masses[i] * positions[i]
            center_of_mass /= total_mass
            features.extend(center_of_mass)
            
            # 质心速度
            center_of_velocity = np.zeros(3)
            for i in range(3):
                center_of_velocity += masses[i] * velocities[i]
            center_of_velocity /= total_mass
            features.extend(center_of_velocity)
            
            # 添加10%的标签噪声
            if random.random() < 0.1:
                label = 1 - label
            
            # 添加特征
            features.append(label)
            data.append(features)
            label_counts[label] += 1
    
    return data

def generate_fruit_dataset(num_samples=200, noise_level=0.1):
    """
    生成带随机扰动的水果识别数据集
    特征: [R, G, B, 重量(g), 直径(cm), 纹理, 产地, 是否有斑点/条纹, 标签]
    标签: 0=苹果, 1=香蕉, 2=橙子, 3=梨
    """
    data = []
    
    # 水果特征范围定义
    fruit_rules = {
        # 苹果
        0: {
            'color': [(255, 0, 0), (0, 255, 0)],  # 红色或绿色
            'weight': (100, 200),
            'diameter': (6.5, 8.5),
            'texture': ['光滑', '轻微粗糙'],
            'origin': ['温带'],
            'spots': ['否'],
            'color_variation': 30,  # 颜色变化范围
            'size_variation': 0.15   # 尺寸变化比例
        },
        # 香蕉
        1: {
            'color': [(255, 255, 0)],  # 黄色
            'weight': (110, 140),
            'diameter': (17, 22),
            'texture': ['光滑'],
            'origin': ['热带'],
            'spots': ['否'],
            'color_variation': 20,
            'size_variation': 0.25
        },
        # 橙子
        2: {
            'color': [(255, 165, 0)],  # 橙色
            'weight': (150, 200),
            'diameter': (7, 9),
            'texture': ['轻微粗糙'],
            'origin': ['亚热带'],
            'spots': ['否'],
            'color_variation': 15,
            'size_variation': 0.1
        },
        # 梨
        3: {
            'color': [(0, 255, 0), (255, 255, 0)],  # 绿色或黄色
            'weight': (130, 170),
            'diameter': (6, 7.5),
            'texture': ['光滑'],
            'origin': ['温带'],
            'spots': ['是'],
            'color_variation': 25,
            'size_variation': 0.2
        }
    }
    
    # 类别编码
    texture_map = {'光滑': 0, '轻微粗糙': 1, '非常粗糙': 2, '有绒毛': 3}
    origin_map = {'热带': 0, '温带': 1, '亚热带': 2}
    spots_map = {'否': 0, '是': 1}
    
    # 生成每个类别相同数量的样本
    samples_per_class = num_samples // len(fruit_rules)
    
    for fruit_type, rules in fruit_rules.items():
        for _ in range(samples_per_class):
            # 随机选择一个基础颜色
            base_color = random.choice(rules['color'])
            
            # 添加颜色随机扰动
            r = max(0, min(255, base_color[0] + random.randint(-rules['color_variation'], rules['color_variation'])))
            g = max(0, min(255, base_color[1] + random.randint(-rules['color_variation'], rules['color_variation'])))
            b = max(0, min(255, base_color[2] + random.randint(-rules['color_variation'], rules['color_variation'])))
            
            # 添加尺寸随机扰动
            weight = random.uniform(rules['weight'][0], rules['weight'][1])
            weight *= (1 + random.uniform(-rules['size_variation'], rules['size_variation']))
            
            diameter = random.uniform(rules['diameter'][0], rules['diameter'][1])
            diameter *= (1 + random.uniform(-rules['size_variation'], rules['size_variation']))
            
            # 选择其他特征
            texture = random.choice(rules['texture'])
            origin = random.choice(rules['origin'])
            spots = random.choice(rules['spots'])
            
            # 添加噪声
            if random.random() < noise_level:
                # 随机改变一个特征
                feature_to_change = random.choice(['color', 'weight', 'diameter', 'texture', 'origin', 'spots'])
                
                if feature_to_change == 'color':
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                elif feature_to_change == 'weight':
                    weight = random.uniform(50, 300)
                elif feature_to_change == 'diameter':
                    diameter = random.uniform(3, 25)
                elif feature_to_change == 'texture':
                    texture = random.choice(['光滑', '轻微粗糙', '非常粗糙', '有绒毛'])
                elif feature_to_change == 'origin':
                    origin = random.choice(['热带', '温带', '亚热带'])
                elif feature_to_change == 'spots':
                    spots = random.choice(['是', '否'])
            
            # 10%的概率翻转标签
            true_label = fruit_type
            if random.random() < noise_level:
                label = random.choice([l for l in fruit_rules.keys() if l != fruit_type])
            else:
                label = fruit_type
            
            # 转换为数值编码
            texture_code = texture_map[texture]
            origin_code = origin_map[origin]
            spots_code = spots_map[spots]
            
            # 添加到数据集
            data.append([r, g, b, weight, diameter, texture_code, origin_code, spots_code, label])
    
    return data