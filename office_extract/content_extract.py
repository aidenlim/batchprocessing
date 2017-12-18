#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
from collections import defaultdict as dd


def pair_off(filelist):
    filepairs = dd(list)
    for file in filelist:
        filepairs[file.header].append(file)

    for k, v in filepairs.items():
        if len(v) != 2:
            sys.stderr.write(k)
        else:
            if v[0].lang == 'ja':
                print(v[0].orig, v[0].fullpath)
                align = run_aligner(k, v[0], v[1])
            else:
                align = run_aligner(k, v[1], v[0])

            if align == b'':
                sys.stderr.write(k + '\n')
            else:
                # todo: logging
                continue


def run_aligner(header, jafile, enfile):
    align_output = subprocess.check_output([
        # todo: set aligner path and outputdir
        '/home/aiden/Downloads/align-all-170804E/align.sh',
        'ja-en',
        jafile.fullpath,
        enfile.fullpath,
        '/home/aiden/Documents/toyota/ttdc/alignout/' + header + '.align.out',
        '--db'
    ])

    return align_output


def prepare_dir(filedir):
    filelist = os.listdir(filedir)

    pairlist = []
    unklist = []
    for f in filelist:
        if f.endswith('.txt') and (f.startswith('w') or f.startswith('e')):
            pairlist.append(FileProp(filedir + f))
        else:
            unklist.append(f)

    if len(unklist) != 0:
        sys.stderr.write('Logging files with Unknown Headers')
        # todo: add logging here
    return pairlist


class FileProp:
    def __init__(self, file):
        fname, flang = self.get_name(file)

        self.orig = file
        self.fullpath = os.path.abspath(file)
        self.header = fname

        if flang == 'w':
            self.lang = 'ja'
        elif flang == 'e':
            self.lang = 'en'
        else:
            self.lang = 'unk'

    @staticmethod
    def get_name(filename):
        filepath = filename.split('.')
        fullname = '.'.join(filepath[:-1])
        nameparts = fullname.split('_')
        lang = nameparts[0]
        name = '_'.join(nameparts[1:])

        return name, lang


if __name__ == "__main__":
    location = sys.argv[1]
    filelist = prepare_dir(location)
    pair_off(filelist)