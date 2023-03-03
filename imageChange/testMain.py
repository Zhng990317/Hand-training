# -*-coding:utf-8 -*-
# @Date: 2023/2/16 19:43
# @File: testMain
from AuthFrame import AuthFrame

ROW_LABLES = ['序号', '名称', '服务器名称', '路径', '请求头信息', '请求参数', '断言文本', '结果']

if __name__ == '__main__':
    AuthFrame('G:\\123.xlsx', '123').create_file(ROW_LABLES)
    print(AuthFrame('G:\\123.xlsx', '123').read_file(None, 2))