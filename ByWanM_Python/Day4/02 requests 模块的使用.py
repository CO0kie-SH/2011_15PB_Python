# requests 是一个第三方模块，需要使用 pip 进行安装
import requests

# 定义一个需要被爬取的网页
url = 'http://47.94.87.68'

# 自定义的 http header，可以添加自己的内容
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'k1': 'v1'
}

# 自定义的参数，需要提供给 params
params = {'k1': 'v1', 'k2': 'v2'}
data = {'k1': 'v1', 'k2': 'v2'}

# requests.请求方式 可以指定请求方式访问目标网页
content = requests.get(url=url, headers=headers, params=params)
print(content.text)

# 使用 post 的方式访问目标页面，data 和 params 分别提供 psot 和 get 参数
content = requests.post(url=url, headers=headers, params=params, data=data)
print(content.text)

# 输出返回给我们的信息
print(content.text)             # 解码后的
print(content.content)          # 解码前的
print(content.status_code)      # 状态码
print(content.headers)          # 响应头
