#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re

__author__ = 'yinshuai'


re_yymmdd = re.compile(r'[\s\S]*[${]([\d-]+)d[_]yyyymmdd[}][\s\S]*', re.S)   # 用于匹配yyyyMMdd格式数据
re_yy_mm_dd = re.compile(r'[\s\S]*[${]([\d-]+)d[_]yyyy-mm-dd[}][\s\S]*', re.S)  # 用于匹配yyyy-MM-dd格式数据
re_pt = re.compile(r'[\s\S]*[${]([\d-]+)d[_]pt[\s\S]*', re.S)  # 用于匹配d_pt格式数据

# 反向转化　
re_pt_real = re.compile(r'[\s\S]*([\d]{8}000000)')
re_yymmdd_real = re.compile(r'[\s\S]*(20[\d]{2}[\d]{2}[\d]{2})[\s\S]*')
re_yy_mm_dd_real = re.compile(r'[\s\S]*(20[\d]{2}-[\d]{2}-[\d]{2})[\s\S]*')

# 年月格式
re_yy_mm_real = re.compile(r'[\s\S]*(20[\d]{2}-[\d]{2})[^-\d][\s\S]*')
re_yymm_real = re.compile(r'[\s\S]*(20[\d]{2}[\d]{2})[^-\d][\s\S]*')

# 年月格式
re_yy_mm_real = re.compile(r'[\s\S]*(20[\d]{2}-[\d]{2})[^-\d][\s\S]*')
re_yymm_real = re.compile(r'[\s\S]*(20[\d]{2}[\d]{2})[^-\d][\s\S]*')


def get_real_time(date_format, time_range):
    """
    根据不同的分区范围来获取特定格式的日期
    :param date_format 日期格式
    :param time_range 日期范围
    :return: exg:
    """
    date_info = datetime.datetime.now() - datetime.timedelta(days=time_range)
    format_time = date_info.strftime(date_format)
    return format_time

def cal_timedelta(start_date, end_date, time_format, type='d'):
    """
    计算两个之间的天数间隔
    :param start_date:
    :param end_date:
    :param time_format:
    :param type: 计算类型，包含d(day),m(month),y(year)
    :return:
    """
    start = datetime.datetime.strptime(start_date, time_format)
    end = datetime.datetime.strptime(end_date, time_format)
    if type == 'd':
        return (end - start).days
    if type == 'm':
        pass


def get_format_now(time_format):
    """
    生成当前日期的指定格式
    :param time_format:
    :return:
    """
    return datetime.datetime.strftime(datetime.datetime.now(), time_format)


def get_shell_from_real(date_format, time_info):
    """
    将具体的时间分区转化为shell分区格式
    :param date_format:　日期格式
    :return: time_info 时间内容
    """
    if date_format == '%y%m%d000000':
        pass

    raise ValueError("date_format is not correct")


def cal_month_delta(date_cal, date_format):
    """
    计算输入日期距离今天月份差
    :param date_cal:　输入月份
    :param date_format: 日期格式
    :return: 月份差
    """
    date_now = datetime.datetime.today()
    date_cal = datetime.datetime.strptime(date_cal, date_format)
    return (date_cal.year - date_now.year) * 12 + (date_cal.month - date_now.month)


if __name__ == '__main__':
    the_str = "where pt= '20181111' and first_visit_date='2018-11-11' and dp '20181105000000' '20181105000000'in ('app') and pt = '20181105000000'"