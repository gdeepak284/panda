import xlrd
import json, requests
import boto3, botocore
from boto3.s3.transfer import S3Transfer
import os


class Panda:
    aws_access_key_id = 'AKIAICLQ6KXAX6TLKV2Q'
    aws_secret_access_key = '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'
    bucket_name = 'pandadeepak'
    xls_filepath = 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'
    s3 = boto3.client("s3",
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)

    def panda(self):
        print("Downloading the xls sheet from net")
        resp = requests.get(self.xls_filepath)
        with open("asd.xls", 'wb') as f:
            f.write(resp.content)

        book = xlrd.open_workbook(os.getcwd() + "/asd.xls")
        sheet = book.sheet_by_name('MICs List by CC')
        keys = [str(sheet.cell(0, col_index).value) for col_index in
                range(sheet.ncols)]

        print("Making the json file")
        dict_list = []
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                 for col_index in range(sheet.ncols)}
            dict_list.append(d)

        with open('employees.json', 'w') as fout:
            json.dump(dict_list, fout, indent=4)

        transfer = S3Transfer(self.s3)
        transfer.upload_file(os.getcwd() + '/employees.json',
                             self.bucket_name,
                             "employees.json")


if __name__ == "__main__":
    p = Panda()
    p.panda()
