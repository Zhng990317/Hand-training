# -*-coding:utf-8 -*-
# @Date: 2023/2/16 16:10
# @File: CreateFile

import os

import xlrd, xlwt


class Create(object):

    TABLE_TYPE = ['.xlsx', '.xls', '.csv']

    def __init__(self, file_path, sheet_name, labels: list = None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.labels = labels

    #   self.create_file()
    #
    # def create_file(self):
    #     with open(self.file_path, 'w', encoding='UTF-8') as f:
    #         pass

    def set_up_excel(self):
        if os.path.splitext(self.file_path)[1] not in self.TABLE_TYPE:
            exit(0)
        try:
            workbook = xlwt.Workbook(encoding="UTF-8")
            worksheet = workbook.add_sheet(sheetname=self.sheet_name)

            style = xlwt.XFStyle()
            pattern = xlwt.Pattern()
            pattern.pattern = xlwt.Pattern.SOLID_PATTERN
            pattern.pattern_fore_colour = 18
            font = xlwt.Font()
            font.name = "宋体"

            font.colour_index = 1
            style.font = font
            style.pattern = pattern

            if self.labels is not None:
                for col in range(0, len(self.labels)):
                    worksheet.write(0, col, self.labels[col], style)
            else:
                worksheet.write(0, 0, '', style)
            workbook.save(self.file_path)

        except:
            print("表格操作出错！")

    def set_up_yml(self):
        pass
