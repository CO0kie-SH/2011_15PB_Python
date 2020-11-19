import time

# 获取当前的时间戳(使用浮点数记录的秒数)
print(time.time())

# 将指定的时间戳转换为当前时区的元组
print(time.localtime())
print(time.gmtime())        # 标准时区

# 将时间元组转换为时间戳
print(time.mktime(time.localtime()))

# 睡眠一定的时间
time.sleep(0.500)

# 将时间元组转换成时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))