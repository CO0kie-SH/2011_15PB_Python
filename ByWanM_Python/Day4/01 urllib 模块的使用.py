# urllib 是 python 内置的一个模块，提供了基本的 http 请求操作

# urllib.request 提供的就是基本的 http 请求操作
import urllib.request
# urllib.parse 提供了 url 中参数的解析功能
import urllib.parse


# 定义一个需要被爬取的网页
url = 'http://47.94.87.68'

# 自己打包 url 中的参数信息，组合成 k1=v1&k2=v2 的形式，需要自己使用 ? 进行拼接
url += '?' + urllib.parse.urlencode({'k1': 'v1', 'k2': 'v2'})

# 自定义的 http header，可以添加自己的内容
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'k1': 'v1'
}

# Request 返回的是一个请求对象，可以添加自定义的头部，通过 data 可以设置 post 参数
request = urllib.request.Request(url=url, headers=headers, data=b'k1=v1&k2=v2')

# 可以使用 request 对象动态的添加 http 数据
request.add_header('k2', 'v2')

# 如果传递的参数是 url，那么就会直接访问网页，并返回内容对象
# 直接使用 urlopen 实际上并不能自定义头部，需要依赖于 request
content = urllib.request.urlopen(request)

print(content.read().decode())
print(content.info())
print(content.getcode())
print(content.geturl())


# 直接访问 + 自定义 header 访问 + 添加 get 参数 + 添加 post 参数 + 添加 header 字段
