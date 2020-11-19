import time
import requests
from bs4 import BeautifulSoup


# 分析并精简链接： https://movie.douban.com/top250?start=？
url_base = r'https://movie.douban.com/top250?start={}'

# 直接访问网页发现没有返回内容，可以认为是 ua 反爬了，所以提供一个 ua
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)'
}

# 保存所有电影的名称
movies_name = []

# 编写一个循环，循环获取到所有共 10 页的数据
for start in range(0, 25, 25):
    # 通过 requests 模块访问目标网页
    content = requests.get(url_base.format(start), headers=headers)

    # 先创建 bs 对象解析网页
    bs = BeautifulSoup(content.text, 'html.parser')

    # 获取到列表中的每一项，每一项保存了电影的所有新
    movie_list = bs.find(class_='grid_view')

    # 获取到 movie_list 里面的每一个 li 项
    items = movie_list.find_all('li')

    # 再通过 find 查找到其中的子元素
    for item in items:
        url = item.select('.hd a')
        # 通过中括号获取标签中的属性
        print(url[0]['href'])

    # 如果爬取的过快，可能对目标服务器造成伤害，时间最好随机
    time.sleep(0.01)


# 遍历电影名称列表，输出所有的名字
for index, name in enumerate(movies_name):
    print(index, name)
