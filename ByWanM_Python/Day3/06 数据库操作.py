# 通过 pymysql 连接并操作 mysql 数据库
import pymysql


class Mysql(object):

    def __init__(self, database_name):
        try:
            # 通过 connect 函数传入数据库的配置信息连接到数据库
            self.connect = pymysql.connect(host='127.0.0.1', user='root',
                password='123456', port=3306, database=database_name)
            # 一旦数据库连接成功，我们就需要获取到游标对象
            self.cursor = self.connect.cursor()
        except Exception as e:
            print('error', e)

    def insert(self, sql: str):
        try:
            self.cursor.execute(sql)
            # 对于所有修改数据库的操作，都需要提交
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            print('error', e)

    def select(self, sql: str):
        try:
            self.cursor.execute(sql)
            # 从数据库中获取到查询的结果集，返回的是一个元组，
            # 元组中的每一个元素表示一行，保存的是一行中的每一列
            result = self.cursor.fetchall()
            count = self.cursor.rowcount
            # 将查询到的行数和内容进行打包，返回给调用方
            return count, result
        except Exception as e:
            print('error', e)


if __name__ == '__main__':
    sql = Mysql('student')
    sql.insert("INSERT INTO stu_class VALUE(10, 'ten')")
    print(sql.select('select * from stu_class;'))