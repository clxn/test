# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:42:36 2016

@author: hutia
"""
import datetime
import re
import FinanceAPI.Config as Config


def is_trading_day(str_date):
    pattern = '^\d{4}-\d{2}-\d{2}$'
    res = re.match(pattern, str_date)
    if res is None:
        raise Exception('invalid date format')
    # function config
    holiday_list = Config.holiday_list
    begin_year = int(holiday_list[0][0:4])
    end_year = int(holiday_list[-1][0:4])
    # start function
    year = int(str_date[0:4])
    if begin_year <= year <= end_year:
        if str_date in holiday_list:
            return False
        weekday = datetime.datetime.strptime(str_date, '%Y-%m-%d').weekday()
        if weekday == 5 or weekday == 6:
            return False
        else:
            return True
    else:
        raise Exception(str_date + ' out of range value for date')


def next_trading_day(str_date):
    pattern = '^\d{4}-\d{2}-\d{2}$'
    res = re.match(pattern, str_date)
    if res is None:
        raise Exception('invalid date format')
    this_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    while True:
        this_date = this_date + datetime.timedelta(days = 1)
        this_str_date = this_date.strftime('%Y-%m-%d')
        if is_trading_day(this_str_date):
            return this_str_date


def previous_trading_day(str_date):
    pattern = '^\d{4}-\d{2}-\d{2}$'
    res = re.match(pattern, str_date)
    if res is None:
        raise Exception('invalid date format')
    this_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    while True:
        this_date = this_date - datetime.timedelta(days = 1)
        this_str_date = this_date.strftime('%Y-%m-%d')
        if is_trading_day(this_str_date):
            return this_str_date
            

def get_trading_day(begin_date, end_date):
    trading_day_list = []
    if is_trading_day(begin_date):
        trading_day_list.append(begin_date)
    next_ = begin_date
    while next_ <= end_date:
        next_ = next_trading_day(next_)
        if next_ <= end_date:
            trading_day_list.append(next_)
    return trading_day_list


def get_last_n_trading_day(str_date, n_days):
    trading_day_list = []
    n_trading_day = 0
    if is_trading_day(str_date):
        trading_day_list.append(str_date)
        n_trading_day += 1
    pre_  = str_date
    while n_trading_day < n_days:
        pre_ = previous_trading_day(pre_)
        trading_day_list.append(pre_)
        n_trading_day += 1
    trading_day_list.sort()
    return trading_day_list


if __name__ == "__main__":
    print(get_trading_day('2016-11-03', '2016-11-09'))
    print(get_last_n_trading_day('2016-11-13', 5))
    print(next_trading_day('2000-01-01'))


