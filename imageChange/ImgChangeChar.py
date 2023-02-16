from PIL import Image


class imgChangeChar:
    char_set = '01'
    img = r'C:\Users\NineZhang\Pictures\Camera Roll\uwp3024212.jpeg'
    # 打开图片
    im = Image.open(img)
    # 缩小图片
    im = im.resize((80, 80), Image.NEAREST)
    # 黑白化
    im = im.convert("L")

    # 字符替换像素点
    def get_char(self, gray):
        if gray >= 240:
            return ' '
        else:
            return imgChangeChar.char_set[int(gray / ((256.0 + 1) / len(imgChangeChar.char_set)))]

    text = ''
    # 获取像素点
    for i in range(im.height):
        for j in range(im.width):
            gray = im.getpixel((j, i))  # 返回值可能是一个int, 也可能是一个三元组
            if isinstance(gray, tuple):
                gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 0.0722 * gray[2])

            text += get_char(gray)
        text += '\n'

    with open(r'C:\Users\NineZhang\Desktop\123.txt', 'w') as f:
        f.write(text)
