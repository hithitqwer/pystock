#coding:utf-8
import tushare as ts


#一段小脚本，把笔记里面记录的红电波推荐的票，计算下3，5，10日内的价格变动情况
#example: 海南瑞泽  2018-02-26（推荐买入时间）

hn=ts.get_k_data('002596',start='2018-02-26',end='2018-03-01')

print hn

a='test'
print a