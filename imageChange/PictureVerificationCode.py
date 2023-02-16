# -*-coding:utf-8 -*-
# @Date: 2023/2/6 18:57
# @File: PictureVerificationCode
import base64
import os
import random
import string
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


class PictureVerificationCode:

    def __init__(self):
        pass

    def randomColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def generationPicture(self, height=10, width=20):
        img_1 = Image.new('RGB', (width, height), self.randomColor())
        return img_1

    def randomString(self):
        # string.ascii_letters生成字母a-z、A-Z；string.digits：生成数字0-9
        verification_code = random.choice(string.ascii_letters + "!@#$%^&*()" + string.digits)
        return verification_code

    def drawString(self, image, count=4, font_size=35):
        # C:\Windows\Fonts\palai.ttf
        draw = ImageDraw.Draw(image)
        font_file = r'C:\Windows\Fonts\palai.ttf'
        font = ImageFont.truetype(font_file, size=font_size)
        valid_str = ''
        for i in range(count):
            randomChar = self.randomString()
            draw.text((10 + i * 30, -2), randomChar, self.randomColor(), font=font)
            valid_str += randomChar

        return valid_str, image

    def noise(self, image, width=120, height=35, line_count=3, point_count=20):
        '''

        :param image: 图片对象
        :param width: 图片宽度
        :param height: 图片高度
        :param line_count: 线条数量
        :param point_count: 点的数量
        :return:
        '''
        draw = ImageDraw.Draw(image)
        for i in range(line_count):
            x1 = random.randint(0, width)
            x2 = random.randint(0, width)
            y1 = random.randint(0, height)
            y2 = random.randint(0, height)
            draw.line((x1, y1, x2, y2), fill=self.randomColor())

            # 画点
            for i in range(point_count):
                draw.point([random.randint(0, width), random.randint(0, height)], fill=self.randomColor())
                x = random.randint(0, width)
                y = random.randint(0, height)
                draw.arc((x, y, x + 4, y + 4), 0, 90, fill=self.randomColor())

        return image

    def valid_code(self):
        """
        生成图片验证码,并对图片进行base64编码
        :return:
        """
        image = self.generationPicture()
        valid_str, image = self.drawString(image, 4, 35)
        image = self.noise(image)
        image.save(r'C:\Users\NineZhang\Desktop\a.jpg')

        f = BytesIO()
        image.save(f, 'png')  # 保存到BytesIO对象中, 格式为png
        data = f.getvalue()
        f.close()

        encode_data = base64.b64encode(data)
        data = str(encode_data, encoding='utf-8')
        img_data = "data:image/jpeg;base64,{data}".format(data=data)
        return valid_str, img_data

if __name__ == '__main__':
    img = PictureVerificationCode().generationPicture()
    img.save(r'C:\Users\NineZhang\Pictures\新建文件夹\2.png')
    # print(PictureVerificationCode().valid_code())