import json
import requests

# 直接访问网页发现没有返回内容，可以认为是 ua 反爬了，所以提供一个 ua
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)'
}

# 直接使用链接会发现爬取不到想要的数据，原因是网页使用了 ajax 技术，实际的数据是通过 js 动态
# 请求并添加到 DOM 节点中的，所以直接抓取网页无效，需要分析 js 请求的 url，抓包分析的过程中
# 如果猜测是 ajax 返回的数据可以尝试筛选出 xhr 类型的数据，或者使用关键字 list 查找数据
url_base = "https://movie.douban.com/j/chart/top_list?type=14&interval_id=100%3A90&start={}&limit=10"


for start in range(0, 100, 10):
    content = requests.get(headers=headers, url=url_base.format(start))
    movies_json = json.loads(content.text)

    for movie in movies_json:
        print(movie['title'], movie['rating'], movie['release_date'])