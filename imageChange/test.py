# def print_list(list_a:list,list_b:list):
#     for i in list_a:
#         if isinstance(i, int):
#             temp = list_a.pop()
#             list_b.append(temp)
#     return list_b

# list_a = [1, 2,'3']
# list_b = []
# print(print_list(list_a[:], list_b))
# print(list_a)
# def print_dict(**dict_a):
#     dict_temp = {}
#     dict_temp['first_name'] = 'liu'
#     dict_temp['last_name'] = 'xing'
#     for i , k in dict_a.items():
#         dict_temp[i] = k
#     return dict_temp

# print(print_dict(full_name = 'liuxing'))
from collections import OrderedDict
import json

dict_a = {
    "en":3,
    "ai":1,
    "if":4,
    "bi":2
}
# dict_b = {}
# # for i in sorted(dict_a.keys()):
# #     dict_b[i] = dict_a[i]
# print(dict_a)
# print(dict_b)

# dict_c = {}
# dict_c['fd'] = 12
# dict_c["ac"] = 1
# dict_c['eg']= 'her'
# for k,v in dict_c.items():
#     print(k + ' = ' + str(v))
with open(r'E:\GIT\新建文件夹\测试用文件.json','a',encoding='utf-8') as f:
    json.dump(dict_a, f)

with open(r'E:\GIT\新建文件夹\测试用文件.json') as f:
    print(json.load(f))