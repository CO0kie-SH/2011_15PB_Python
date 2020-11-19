import hashlib
m = hashlib.md5()
m.update(b'123')
print(m.hexdigest())
print(hashlib.md5(b'123').hexdigest())

import base64
url = "https://www.cnblogs.com/songzhixue/"
bytes_url = url.encode("utf-8")
str_url = base64.b64encode(bytes_url) # 被编码的参数必须是二进制数据
print(str_url)
str_url = base64.b64decode(url).decode("utf-8")
print(str_url)
