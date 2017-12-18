#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging

top_dir = os.path.dirname(os.path.abspath(__file__))

log_folder = top_dir + '/log/'


class BasicLog(object):
    log_format = logging.Formatter('%(asctime)s | %(name)-15s - %(process)d | %(levelname)-9s| %(message)s')


class DebugLog(BasicLog):
    log_handler = logging.FileHandler(log_folder + 'debug.log', mode='a')
    log_level = logging.DEBUG


class InfoLog(BasicLog):
    log_handler = logging.FileHandler(log_folder + 'info.log', mode='a')
    log_level = logging.INFO
