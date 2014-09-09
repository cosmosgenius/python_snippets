import xlrd
import json
import sys
import argparse


def convert(workbook):
    wb = xlrd.open_workbook(workbook)
    data = []
    for month in wb.sheet_names():
        sheet_obj = wb.sheet_by_name(month)
        if sheet_obj.nrows == 0:
            break
        expense_name = sheet_obj.row_values(0)[2:]
        for i in range(2, sheet_obj.nrows):
            row = sheet_obj.row_values(i)
            date = xlrd.xldate_as_tuple(row[0], 0)[2]
            year = xlrd.xldate_as_tuple(row[0], 0)[0]
            expense_object = {}
            for index, value in enumerate(row[2:]):
                if value != '':
                    expense_object[expense_name[index]] = value
            json_object = {u'year': year, u'month': month, u'date': date, u'expense': expense_object}
            data.append(json_object)
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Expense Sheet to json')
    parser.add_argument('workbook', help='Expense Sheet filename')
    parser.add_argument('-j', metavar='jsonfile', default='data.json', help='outfile json filename', dest='outputfile')
    args = parser.parse_args()
    if args.workbook:
        with open(args.outputfile, 'w') as outfile:
            data = convert(args.workbook)
            json.dump(data, outfile, indent=4, separators=(',', ': '))
    else:
        parser.print_help()
        sys.exit()
