import re
import requests

# 分析并精简链接： https://movie.douban.com/top250?start=？
url_base = r'https://movie.douban.com/top250?start={}'

# 直接访问网页发现没有返回内容，可以认为是 ua 反爬了，所以提供一个 ua
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)'
}

# 保存所有电影的名称
movies_name = []

# 编写一个循环，循环获取到所有共 10 页的数据
for start in range(0, 250, 25):
    # 通过 requests 模块访问目标网页
    content = requests.get(url_base.format(start), headers=headers)
    movies_name += re.findall(r' class="">\s*<span class="title">(.*?)</span>', content.text)

# 遍历电影名称列表，输出所有的名字
for index, name in enumerate(movies_name):
    print(index, name)
