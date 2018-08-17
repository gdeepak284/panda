import xlrd
import json


def read_the_file(path='/Users/user/Downloads/input.csv'):
    with open(path, 'r') as f:
        loc = '/Users/user/Downloads/ISO10383_MIC.xls'
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("MICs List by CC")
        sheet.cell_value(0, 0)
    return sheet

if __name__ == "__main__":
    book = xlrd.open_workbook('/Users/user/Downloads/ISO10383_MIC.xls')
    sheet = book.sheet_by_name('MICs List by CC')
    keys = [str(sheet.cell(0, col_index).value) for col_index in range(sheet.ncols)]

    dict_list = []
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in range(sheet.ncols)}
        dict_list.append(d)

    with open('employees.json', 'w') as fout:
        json.dump(dict_list, fout, indent=4)
