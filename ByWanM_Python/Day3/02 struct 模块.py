# 通过 struct 可以实现字节流到结构体的转换
import struct

# 打包成 int + int + char[1024] 的结构体
bytes_content = struct.pack('ii1024s', 10, 20, b'hello15pb')
print(bytes_content)

# 将 nt + int + char[1024] 的结构体进行解包
type, length, content = struct.unpack('ii1024s', bytes_content)
print(type, length, content.decode('utf8').strip('\0'))

