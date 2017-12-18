#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
# from ttdc.config import top_dir

convert_dir = '/home/aiden/Documents/toyota/ttdc' + '/converted'

if not os.path.isdir(convert_dir):
    subprocess.run(['mkdir', convert_dir])


def file_convert(file):
    convert_out = subprocess.check_output([
        'off2txt',
        '-d',
        convert_dir,
        file
    ])

    return convert_out


def xlsx_convert(file, fileheader):
    filename, ext = os.path.splitext(fileheader)
    convert_out = subprocess.check_output([
        'xlsx2csv',
        file,
        convert_dir + '/' + filename + '.csv'
    ])

    return convert_out

# def x_convert(file):
#     if not file.endswith('x'):
#         filename, ext = os.path.splitext(file)
#         soffice_out = subprocess.check_output([
#             'libreoffice',
#             '--headless',
#             '--convert-to',
#             ext + 'x',
#             file
#         ])
#         final = file + 'x'
#         print(soffice_out)
#
#     else:
#         final = file
#
#     return final


if __name__ == "__main__":
    filelist = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
    for file in filelist:
        if file.endswith('x'):
            if file.endswith('xlsx'):
                convert = xlsx_convert(os.path.join(sys.argv[1], file), file)
            else:
                convert = file_convert(os.path.join(sys.argv[1], file))
            if convert == b'':
                sys.stdout.write(file + '\n')
            else:
                sys.stderr.write(convert + '\n')
