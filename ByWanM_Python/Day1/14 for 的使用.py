l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 使用 for 遍历的几种方式: 值的遍历
for item in l:
    print(item, end=' ')
print('')

# 使用下标的方式进行遍历
for index in range(len(l)):
    print(f'l[{index}]={l[index]}', end=' ')
print('')

# 通过枚举的方式进行索引
for index, item in enumerate(l):
    print(f'l[{index}]={item}', end=' ')
print('')

d = {'小明': 100, "小红": 101, '小刚': 99}

# 字典的遍历方式: 键，默认使用字典名就是 keys
for key in d.keys():
    print(f'd[{key}]={d[key]}', end=' ')
print('')

# 字典的遍历方式: 值
for value in d.values():
    print(f'{value}', end=' ')
print('')

# 字典的遍历方式: 键值对
for key, value in d.items():
    print(f'd[{key}]={value}', end=' ')
print('')