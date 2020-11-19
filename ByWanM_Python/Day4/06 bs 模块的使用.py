# bs4 是一个用于爬取网页的第三方库，可以根据提供的标签，id 和类名等抓取数据
from bs4 import BeautifulSoup

html = """
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>demo page</title>
</head>
<body>
    <ul id="myid">
        <li class="myclass">ul 第一项</li>
        <li>ul 第二项</li>
        <li class="myclass" id="myid">ul第三项</li>
    </ul>
    <ol id="myid">
        <li class="myclass">ol第一项</li>
        <li>ol第二项</li>
        <li class="myclass">ol第三项</li>
    </ol>
</body>
</html>
"""

# 创建一个基于内置解析器的 bs 对象，用于分析 html 网页
bs = BeautifulSoup(html, 'html.parser')

# 直接传入一个参数，表示查找到的是标签
ul = bs.find_all('ul')
print(ul)

# 可以指定 id 的查找
myid = bs.find_all(id='myid')
print(myid)

# 可以指定 class 的查找
myclass = bs.find_all(class_='myclass')
print(myclass)

# 可以同时指定所有的选项
ul = bs.find_all('li', id='myid', class_='myclass')
print(ul)

# 通过 find_all 返回的一系列对象本身又是一个节点，所以还可以继续查找
