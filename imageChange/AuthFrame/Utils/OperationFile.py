# -*-coding:utf-8 -*-
# @Date: 2023/2/17 16:25
# @File: OperationFile
import os
import traceback
import xlwt, xlrd

TABLE_TYPE = ['.xlsx', '.xls', '.csv']


class Operation(object):

    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        if os.path.splitext(self.file_path)[1] not in TABLE_TYPE:
            print('文件格式错误！')
            exit(0)
        self.sheet_name = sheet_name

    def create_file(self, labels: list = None):
        '''
        创建表格文件
        :param labels: 首行内容
        '''
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

            if labels is not None:
                for col in range(0, len(labels)):
                    worksheet.write(0, col, labels[col], style)
            else:
                worksheet.write(0, 0, '', style)
            workbook.save(self.file_path)
        except:
            print(traceback.format_exc(), "\n表格操作出错！")

    def read_file(self, row=None, col=None):
        '''
        获取表格数据
        :param row: 指定行，可为None
        :param col: 指定列，可为None
        :return: 返回列表类型的表格数据
        '''
        try:
            workbook = xlrd.open_workbook(filename=self.file_path)
            if self.sheet_name not in workbook.sheet_names():
                print('表格名称错误！')
                exit(0)
            table = workbook.sheet_by_name(sheet_name=self.sheet_name)
            table_row0_list = table.row_values(0, 0, table.ncols)
            cell_dict, cell_row = {}, []
            if row not in range(table.nrows) or col not in range(table.ncols):
                for r in range(1, table.nrows):
                    for c in range(table.ncols):
                        cell_dict[table.cell_value(0, c)] = table.cell_value(r, c)
                    cell_row.append(str(cell_dict))
            else:
                table_rowCustom_col = table.row_values(row)
                cell_dict = dict(zip(table_row0_list, table_rowCustom_col))
                cell_row.append(str(cell_dict))
            return cell_row
        except:
            print(traceback.format_exc())

    def edit_file(self, row, col, labels: dict):
        try:
            workbook = xlwt.Workbook(encoding="UTF-8")
            worksheet = workbook.add_sheet(sheetname=self.sheet_name, cell_overwrite_ok=False)

            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            font.name = "宋体"
            font.colour_index = 2
            style.font = font

            if labels is not None:
                for col in range(0, len(labels)):
                    worksheet.write(0, col, labels[col], style)
            else:
                worksheet.write(0, 0, '', style)
            workbook.save(self.file_path)
        except:
            print(traceback.format_exc(), "\n表格操作出错！")

    def delete_file(self):
        return
