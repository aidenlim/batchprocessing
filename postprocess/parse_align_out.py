#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import csv
import logging

logging.basicConfig(filename='extracter.log', level=logging.DEBUG, format='%(asctime)s\t%(levelname)s\t%(message)s')


def output_break(line):
    try:
        (score, title, breakdown, text1, text2) = line.strip().split('|||')
    except ValueError:
        components = line.strip().split('|||')
        text1 = components[-2]
        text2 = components[-1]
        breakdown = components[-3]

    if breakdown != ' 1-1 ':
        flag = False
    else:
        flag = True

    return text1.lstrip().rstrip(), text2.lstrip().rstrip(), flag


def file_process(inputfile):
    parallel_output = []
    multiple_output = []
    with open(inputfile, 'r') as infile:
        for line in infile:
            (source, target, count) = output_break(line)
            if count:
                parallel_output.append((source, target))
            else:
                multiple_output.append((source, target))

    return parallel_output


def corpus_write(parallels, outputfile):
    with open(outputfile, 'w') as outfile:
        parallelwriter = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for parallel in parallels:
            parallelwriter.writerow([parallel[0], parallel[1]])
    logging.info('Parsed and Wrote {0}'.format(outputfile))


if __name__ == "__main__":
    alignfilelist = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
    for alignmentfile in alignfilelist:
        prefix = alignmentfile.split('.')[0]
        data = file_process(alignmentfile)
        corpus_write(data, prefix + '.align.csv')
