# python 提供了 re 模块支持模式匹配（正则表达式）
import re

'''
    普通字符的搜索和字符串搜索完全一致，所以我们主要看特殊字符的使用

    说明位置的特殊字符
    -   ^表示行首：     ^hello 匹配 hellohello 中的第一个 hello
    -   $表示行尾       hello$ 匹配 hellohello 中的第二个 hello

    说明数量的特殊字符
    -   ?:          表示 0 个或者 1 个，例如 ab?c 匹配 ac 和 abc
    -   +:          表示 1 个或更多个，例如 ab+c 匹配 abc\abbc\ab...c
    -   *:          表示 0 个或更多个，例如 ab*c 匹配 ac\abc\ab...c
    -   {n}         表示匹配 n 个， ab{3}c 只匹配 abbbc
    -   {n,}        表示匹配最少 n 个，+ 对应 {1,}，* 对应 {0,}
    -   {n,m}       表示匹配 n 到 m 个，? 匹配 {0,1}

    说明类型的特殊字符
    -   [a-zA-Z]    表示一个大小写字母，例如前面的例子匹配任何一个字母
    -   [^a-z]      表示除了小写的字母以外的所有字符
    -   \d \D       \d 对应 [0-9]， \D 对应[^0-9]
    -   \s \S       \s 对应 [\n\r\t] \S对应[^\n\r\t]
    -   \w \W       \w 对应 [0-9a-zA-Z_] \W 对应[^0-9a-zA-Z_]
    -   .           表示任意一个字符
'''

s1 = '1 + 2 = 3'
s2 = '3a + 4b = 7c'

# 用于判断目标字符串是否和指定的模式匹配
match = re.match(r'(\d) \+ (\d) = (\d)', s1)

# 如果匹配失败，返回 None(False)，否则返回一个匹配对象
if match:
    print(match.span())     # 匹配的范围，起止位置
    print(match.group(0))   # 完整的字符串
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

# 在目标字符串中搜索和模式匹配的一个子串，match 仅匹配开头
match = re.search(r'\d', s2)

# 在目标字符串中搜索和模式匹配的所有个子串
# 如果没有分组，直接返回搜索到的内容，否则返回元组保存每一个分组
find_list = re.findall(r'(\d)([a-c])', s2)
print(find_list)


# 如果传入的是函数，可以根据原数据进行计算
def sub_proc(obj):
    # 从中取出每一组的数据，进行操作并返回
    return str(obj.group(1))*2 + str(obj.group(2)) * 2


# 替换目标字符串中所有和模式匹配的字串
s3 = re.sub(r'(\d)([a-c])', sub_proc, s2)
print(s3)