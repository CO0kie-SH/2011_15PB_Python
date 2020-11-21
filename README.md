# 1118_SQL注入工具

## Ox00 前言

#### 本注入工具可检测

1. [sqli-labs](https://github.com/Audi-1/sqli-labs)->Less-1~Less-10关的注入漏洞
2. [sqlite-lab](https://github.com/incredibleindishell/sqlite-lab)->~~联合注入以及布尔盲注~~

#### 靶场下载链接

> [永硕e盘](http://co0kie.ys168.com/)

#### 项目语雀笔记链接

https://www.yuque.com/co0kie/on3irt/mih4ex

------

## Ox01 食用方法

#### 安装必要第三方库

```
pip install requests
pip install openpyxl
```

或使用豆瓣镜像源安装

```
pip install requests -i http://pypi.douban.com/simple/ 
pip install openpyxl -i http://pypi.douban.com/simple/ 
```

#### 用户参数编辑

- 调整线程数
- 调整时间盲注超时
- xlsx表格导出文件夹
- sqli靶场地链接
- UA设置


#### 启动脚本

- 打开命令行，cd至项目目录，执行python

```powershell
cd /d [项目文件夹]
python main.py
```

或

- 将IDE切换至main.py，执行

> ![image.png](http://img.mhw666.top/myqn/1605928585404-7474b60e-9742-40aa-8fad-ee1b9ec25a7e.png)

- 等待脚本执行

> ![image.png](http://img.mhw666.top/myqn/1605928925568-b8077d32-154a-4d6a-9703-44fb48ea7722.png)

- 输出结果

> ![image.png](http://img.mhw666.top/myqn/1605930314783-acec6100-8178-4987-a378-fa12d6677eb5.png)

- 保存文件

> ![image.png](http://img.mhw666.top/myqn/1605930338451-ffaa66a4-f002-4cf7-88e2-f12c43095f87.png)

- END

------

