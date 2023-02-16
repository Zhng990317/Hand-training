# -*-coding:utf-8 -*-
# @Date: 2023/2/7 10:48
# @File: pictureRename

import os
import uuid


def rename(dir=r'C:\Users\NineZhang\Pictures\Camera Roll'):
    dir_size_dict = {}

    for pic in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, pic)):
            os.rename(os.path.join(dir, pic), os.path.join(dir, str(uuid.uuid4()) + '.jpg'))

    for pic in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, pic)):
            dir_size_dict[pic] = os.path.getsize(os.path.join(dir, pic))
    # 按照第一个元素排序:sorted(A, lambda x:x[0])
    dir_size_dict = sorted(dir_size_dict.items(), key=lambda x: x[1], reverse=False)

    for v in dir_size_dict:
        os.rename(os.path.join(dir, v[0]), os.path.join(dir, str(dir_size_dict.index(v) + 1) + '.jpg'))


rename()
