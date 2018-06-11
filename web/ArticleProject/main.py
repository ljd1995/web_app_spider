#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/6/4 11:45
# @Author  : luojiandong
# @File    : main.py
# @Desc    :
import os
import sys

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute('scrapy crawl 36kr'.split())
