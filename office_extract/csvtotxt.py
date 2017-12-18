#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import os

def get_csv_data(csvfile):
    textdata = []
    with open(csvfile, 'r') as infile:
        data = csv.reader(infile, delimiter=',', quotechar='"')
        for line in data:
            for text in line:
                if text == '' or len(text) == 0:
                    continue
                else:
                    textdata.append(text)

    return textdata


def write_csv_data(data, filedest):
    filedest = filedest.rstrip('.csv')
    filedest = filedest + '.txt'
    with open(filedest, 'w') as outfile:
        for d in data:
            outfile.write(d + '\n')

if __name__ == "__main__":
    filelist = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
    for file in filelist:
        if file.endswith('.csv'):
            textdata = get_csv_data(os.path.join(sys.argv[1], file))
            write_csv_data(textdata, os.path.join(sys.argv[1], file))
            sys.stdout.write(file + '\n')
