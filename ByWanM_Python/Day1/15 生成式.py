# 列表生成式: 快速生成列表
print([i for i in range(1000)])                         # 生成指定序列
print([i for i in range(1000) if i % 2 == 0])           # 生成指定序列 + 判断
print([i**2 for i in range(1000) if i % 2 == 0])        # 生成指定序列 + 判断 + 表达式
print([i*j for i in range(1, 10) for j in range(1, 10)])

import os
dir_base = r'D:\Microsoft\Visual Studio 2019\Common7\IDE\\'
print([os.path.splitext(path) for path in os.listdir(dir_base) if os.path.isfile(dir_base+path)])

# 元组生成式，改成圆括号
# 字典生成式，改成键值对的花括号
# 集合生成式，改成花括号

