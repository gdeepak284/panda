import xlrd
import json
import boto3
from boto3.s3.transfer import S3Transfer


aws_access_key_id= 'AKIAJLQJBMRC7YE6OWOQ'
aws_secret_access_key= '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'
bucket_name ='pandadeepak'


def upload_url_to_s3():
    client = boto3.client('s3',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    transfer = S3Transfer(client)
    transfer.upload_file('/Users/user/Desktop/Assignment',
                         bucket_name,
                         "employees.json")


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

    client = boto3.client('s3',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    transfer = S3Transfer(client)
    transfer.upload_file('/Users/user/Desktop/Assignment/employees.json',
                         bucket_name,
                         "employees.json")
