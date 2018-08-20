import xlrd
import json, requests
import boto3, botocore
from boto3.s3.transfer import S3Transfer
import os


aws_access_key_id = 'xx'
aws_secret_access_key = 'aa'
bucket_name = 'pandadeepak'
xls_filepath = 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'
xls_filepath_local = ''

if __name__ == "__main__":
    # s3 = boto3.client('s3',
    #                   aws_access_key_id=aws_access_key_id,
    #                   aws_secret_access_key=aws_secret_access_key)
    # with open(xls_filepath, "wb") as f:
    #     s3.download_fileobj(bucket_name, aws_access_key_id, f)
    resp = requests.get(xls_filepath)
    s3 = boto3.client("s3",
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    # s3.put_object(Bucket=bucket_name, Key='tmp/ISO10383_MIC.xls')

    with open("asd.xls", 'wb') as f:
        f.write(resp.content)

    # output = open('test.xls', 'wb')
    # output.write(resp.content)
    # output.close()

    book = xlrd.open_workbook(os.getcwd()+"/asd.xls")
    sheet = book.sheet_by_name('MICs List by CC')
    keys = [str(sheet.cell(0, col_index).value) for col_index in
            range(sheet.ncols)]

    dict_list = []
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in range(sheet.ncols)}
        dict_list.append(d)

    with open('employees.json', 'w') as fout:
        json.dump(dict_list, fout, indent=4)

    # s3 = boto3.s3('s3',
    #               aws_access_key_id=aws_access_key_id,
    #               aws_secret_access_key=aws_secret_access_key)
    transfer = S3Transfer(s3)
    transfer.upload_file('/Users/user/Desktop/Assignment/employees.json',
                         bucket_name,
                         "employees.json")
