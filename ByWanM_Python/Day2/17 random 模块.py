import random

# randint 和 randrange
for i in range(100):
    # 生成 0<=value<=10 的一个随机数值
    print(random.randint(0, 10))
    # 先生成一个 range 序列，从中获取一个随机值
    print(random.randrange(0, 10))

# 创建一个字符串，用于保存验证码
tmp = ""
# 主要在于遍历的次数，循环 6 次
for i in range(6):
    # 生成一个满足 range 条件的随机值
    rad1 = random.randrange(4)
    # 有一半的概率进入下面的两个分支
    if rad1 == 1 or rad1 == 3:
        # 生成一个随机的整数并转换为字符串添加到末尾
        rad2 = random.randrange(0, 10)
        tmp += str(rad2)
    else:
        # 生成一个随机的大小字母添加到结尾
        rad3 = random.randrange(65, 91)
        tmp += chr(rad3)
print(tmp)


# 从指定序列中随机取出一个元素
print(random.choice(['饭', '粥', '面', '饿']))

# 打乱一个序列(洗牌)
l = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(l)
print(l)
