#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import sys
import numpy as np
import pandas as pd


stock_list = pd.read_csv('./stock_list.csv', index_col=0, encoding='ANSI')
stock_list.index = map(lambda x: x.lower(), stock_list.index)

today = datetime.date.today().year
file = [str('./data/file/sse/list/%s/%s' % (today, i))
        for i in os.listdir('./data/file/sse/list/%s/' % today) if i.endswith('_temp.csv')]


for i in file:
    data = pd.read_csv(i, header=None, index_col=None, encoding='ANSI', dtype={'code': 'str'}, parse_dates=[
                       5], usecols=[1, 2, 3, 4, 7, 9], names=['code', 'name', 'announcement', 'date', 'link', 'download_time'])
    data.index = map(
        lambda x: x + '.sh' if x[0] == '6' else x + '.sz', data['code'])
    data['code'] = data.index
    if data['download_time'][0] - pd.to_datetime(datetime.datetime.today()) < datetime.timedelta(hours=1):
        group = data.groupby(data['code'])
        for j in group.groups:
            print('\n'.join(list(map(lambda x: '    '.join(x), group.get_group(
                j)[['code', 'name', 'announcement', 'link']].values))))
            text = '\n'.join(list(map(lambda x: '    '.join(x), group.get_group(j)[
                             ['code', 'name', 'announcement', 'link']].values)))
            if j in stock_list.index:
                at_ = stock_list['researcher'][j]
                if not np.isnan(at_):
                    at_ = at_.split('/')
            else:
                print('This stock belongs to no researcher...')
            for researcher_name in at_:
                